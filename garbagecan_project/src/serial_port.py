import serial
import threading
BUFFER = ""
BOOL = True


def openPort(portx, bps, timeout):
    ret = False
    try:
        # open the serial port and get the serial port object
        ser = serial.Serial(portx, bps, timeout=timeout)
        if ser.is_open:
            ret = True
            threading.Thread(target=BUFFER, args=(ser,)).start()
    except Exception as e:
        print("--serial port error--", e)
    return ser, ret


def closePort(ser):
    global BOOL
    BOOL = False
    ser.close()


def readPort():
    global BUFFER
    string = BUFFER
    BUFFER = ""
    return string



