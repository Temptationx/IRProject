from time import sleep
import serial

ser = serial.Serial()


def writeCode(device, code):
    try:
        sb = "\xAA{}{}{}{}".format(chr(code&0xFF), chr((code>>8) & 0xFF), chr((code >> 16) & 0xFF), chr((code >> 24) & 0xFF))
        ser.write(sb)
        print('open', code)
        return True
    except Exception as e:
        print(e)
        return False

def init(device):
    ser.baudrate = 9600
    ser.port = device
    ser.open()
    sleep(1)