#include "mbed.h"
#include "platform/mbed_thread.h"
#include <iostream>
#include <string>

using namespace std;

#define BUFFER_SIZE                                                         3
#define nuclSlav_ADDR                                                       0xB0
#define EEPROM_ADDR                                                         0xA0
#define DS3231_ADDR                                                         0xD0

RawSerial pc(SERIAL_TX, SERIAL_RX);
I2C master(I2C_SDA, I2C_SCL);

DigitalOut led(LED1);
InterruptIn btn(PC_9);

char bufSend[BUFFER_SIZE];      // Configuracion esclavo mbed
char bufReceive[BUFFER_SIZE];

int seg, minu, hora, dia, mes, an;
float ADCdata, ADCvoltaje;

bool btnPress=false, flagSerial=false;
int caracter,limiteSup=0,limiteInf = -10;
char DataRTC[10], data[10], DatoRecibido[10];

void leerRTC();
void ISR_leerRTC();
void ISR_serial();
void corrimiento();
void leer(int bloque);

int main()
{
    /////////////////////////// CONFIGURACION
    //pc.baud(115200);
    pc.attach(&ISR_serial);
    btn.rise(&ISR_leerRTC);
    bufSend[0] = 'm';
    leerRTC();

    while (true) {

////////////////////// BOTON RTC

        if(btnPress) {
            leerRTC();

            for(int i=limiteInf; i<limiteSup; i++) {
                data[0] = 0;                                          // MSB address
                data[1] = i;                                          // LSB address
                data[2] = DataRTC[i%10];                              // data
                pc.printf("%d",DataRTC[i%10]);

                if(master.write(EEPROM_ADDR, data, 3)) {
                    error("Write failed\n");
                }
                while(master.write(EEPROM_ADDR, NULL, 0)); // wait to complete
            }

            btnPress=!btnPress;
        }

//////////////////////////// COMUNICACION SERIAL - COMANDOS //////////////////////////////////////

        else if(flagSerial) {

            if(bufSend[0]==119) {                                       //LECTURA ACD

                master.read(nuclSlav_ADDR, bufReceive, BUFFER_SIZE);
                ADCdata = (bufReceive[0] << 8) + bufReceive[1];
                ADCvoltaje = ADCdata*3.3/65535;
                pc.printf("@%.2f V#\n",ADCvoltaje);
                flagSerial = !flagSerial;
                led = !led;
            }

            else if(bufSend[0]==64) {                                //ENCENDER LED
                master.write(nuclSlav_ADDR, bufSend, BUFFER_SIZE);
                flagSerial = !flagSerial;

            }
////////////////////////////////////////////
            else if(bufSend[0]==49) {                              // LEER DATO ESPECIFICO
                leer(1);
                flagSerial = !flagSerial;
            } else if(bufSend[0]==50) {                              // LEER DATO ESPECIFICO
                leer(2);
                flagSerial = !flagSerial;
            } else if(bufSend[0]==51) {                              // LEER DATO ESPECIFICO
                leer(3);
                flagSerial = !flagSerial;
            } else if(bufSend[0]==52) {                              // LEER DATO ESPECIFICO
                leer(4);
                flagSerial = !flagSerial;
            } else if(bufSend[0]==53) {                              // LEER DATO ESPECIFICO
                leer(5);
                flagSerial = !flagSerial;
            }
//////////////////////////////////////
            else if (bufSend[0]==116) {
                for (int i =1; i<6; i++) {
                    leer(i);
                    thread_sleep_for(500);
                }
                flagSerial = !flagSerial;
            }


            else if (bufSend[0]==101) {

                for(int i=0; i<50; i++) {
                    data[0] = 0;                                          // MSB address
                    data[1] = i;                                          // LSB address
                    data[2] = 255;                                       // data

                    if(master.write(EEPROM_ADDR, data, 3)) {
                        error("Write failed\n");
                    }
                    while(master.write(EEPROM_ADDR, NULL, 0)); // wait to complete

                }
                flagSerial = !flagSerial;
            }

        } else {                                                    // ACTIVACION SERIAL
            pc.printf("r\n");
        }

        thread_sleep_for(200);

    }
}

void leerRTC()             ///////////// LEER RTC Y COLANR ARREGLO GLOBAL
{
    int ret;
    char data_write[2];
    char data_read[10];

    data_write[0] = 0;
    master.write(DS3231_ADDR, data_write, 1, 0);  /// ASEGURAR DIRRECCION SEGUNDOS OXOO

    ret = master.read(DS3231_ADDR, data_read, 7, 0);

    for(int i=0; i<10; i++) {
        DataRTC[i] = data_read[i];     // CLONAR ARREGLO GLOBAL
    }
    //pc.printf("ret = %d, %d-%02d-%02d %d %02d:%02d:%02d\n\r", ret, year, month, date, day, hour, min, sec);
}

void ISR_leerRTC()      //// CAMBIAR LIMITES DEL ARREGLO - SELECCION DE BLOQUES
{
    limiteSup+=10;
    limiteInf+=10;

    if(limiteInf>41) {
        limiteSup=10;
        limiteInf=0;
    }

    btnPress=!btnPress;
}

void ISR_serial()           ////////LEER SERIAL
{
    if (pc.readable()) {
        caracter = pc.getc();
        bufSend[0] = caracter;
        flagSerial = !flagSerial;
    }
}
void corrimiento()   ///// CORRIMIENTO DE DATOS
{

    int sec, min, hour, day, date, month, year;

    sec = (DatoRecibido[0] >> 4) * 10 + (DatoRecibido[0] & 0x0f);
    min = (DatoRecibido[1] >> 4) * 10 + (DatoRecibido[1] & 0x0f);
    hour = (DatoRecibido[2] >> 5 & 0x01) * 20 + (DatoRecibido[2] >> 4 & 0x01) * 10 + (DatoRecibido[2] & 0x0f);

    day = DatoRecibido[3] & 0x07;

    date = (DatoRecibido[4] >> 4) * 10 + (DatoRecibido[4] & 0x0f);
    month = (DatoRecibido[5] >> 4 & 0x01) * 10 + (DatoRecibido[5] & 0x0f);
    year = 2000 + (DatoRecibido[6] >> 4) * 10 + (DatoRecibido[6] & 0x0f);

    seg=sec;
    minu = min;
    hora=hour;
    dia=date;
    mes=month;
    an=year;

    pc.printf("@%d-%02d-%02d %02d:%02d:%02d#\n", an, mes, dia, hora, minu, seg);
}

void leer(int bloque)           ///// LEER DATO ESPECIFICO
{
    int limSup=bloque*10;
    int limInf = limSup-10;

    char response[1];

    data[0] = 0;                                           // MSB address
    data[1] = limInf;                                      // LSB address
    if(master.write(EEPROM_ADDR, data, 2)) {               // ASEGURAR DIRRECION DE LECTURA
        error("Write failed\n");
    }

    for(int i=limInf; i<limSup; i++) {
        if(master.read(EEPROM_ADDR, response, 1)) {
            error("Read failed\n");
        }
        DatoRecibido[i%10]=response[0];
    }
    corrimiento();
}