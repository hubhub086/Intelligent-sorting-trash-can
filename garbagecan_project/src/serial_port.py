import serial
import threading
BUFFER = ""
BOOL = True


def read_data(ser):
    global BUFFER, BOOL
    while BOOL:
        if ser.in_waiting:
            BUFFER = ser.read(ser.in_waiting).decode("gbk")
            print("\n>> receive: ", BUFFER, "\n>>", end="")
            if BUFFER == "quit":
                print("oppo serial has closed.\n>>", end="")


def openPort(portx, bps, timeout):
    ret = False
    ser = serial.Serial()
    try:
        # open the serial port and get the serial port object
        ser = serial.Serial(portx, bps, timeout=timeout)
        if ser.is_open:
            ret = True
            # create a thread to open serial port
            threading.Thread(target=read_data, args=(ser,)).start()
    except Exception as error:
        print("--serial port error--", error)
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


def writePort(ser, text):
    result = ser.write(text.encode("gbk"))
    return result


# if __name__ == "__main__":
#     ser, ret = openPort("/dev/ttyUSB0", 115200, None)
#     if ret:
#         while True:
#             text = input(">>")
#             writePort(ser, text)
#             if text == "quit":
#                 closePort(ser)
#                 print("bye!")
#                 break
