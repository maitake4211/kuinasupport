import serial
ser = serial.Serial('/dev/ttyACM0', 115200)
while True:
    String_data = ser.readline()
    print(String_data)
    with open('Logs/temp.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(String_data)
ser.close()
