#include "mbed.h"
#include "platform/mbed_thread.h"
#define BUFFER_SIZE 3
#define SLAVE_ADDR 0xB0
#define BLINKING_RATE_MS 1000

I2CSlave slave(D14, D15);
DigitalOut led(PB_10);
AnalogIn pot(A0);

RawSerial pc(USBTX, USBRX);

/////////////
int value = 0;
char buf[BUFFER_SIZE] = "AB";
int ADCdataU, ADCdataD;
int a = 0, b = 0;
bool f = 0;
void leer_sensor();

int main()
{
    slave.address(SLAVE_ADDR);
    leer_sensor();

    //pc.baud(9600);
    led=0;
    while (1) {
        int i = slave.receive();
        switch (i) {
            case I2CSlave::ReadAddressed:
                f = 1;
                slave.write(buf, BUFFER_SIZE);

                pc.printf("Enviando al maestro: %s", buf);// CORREGIRRRRRR SE TIENE QUE CREAR char bufSend[BUFFER_SIZE]; // Configuracion esclavo mbed char bufReceive[BUFFER_SIZE];
                break;
            case I2CSlave::WriteGeneral:
                break;
            case I2CSlave::WriteAddressed:
                slave.read(buf, BUFFER_SIZE);
                //pc.printf("Recibido del maestro: %s", buf);
                if (buf[0] == 64) {
                    led=!led;
                }
                break;
        }
        if (f == 1) {
            leer_sensor();
            f = 0;
        }


    }
}
void leer_sensor()
{
    buf[0] = '#';
    value = pot.read_u16();
    ADCdataU = value >> 8;
    ADCdataD = value - (ADCdataU << 8);
    buf[0] = ADCdataU;
    buf[1] = ADCdataD;
    pc.printf("%d \n\r", value);
}