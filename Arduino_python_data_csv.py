import serial
import struct
import csv
import datetime

# Initialize serial connection with increased baud rate
ser = serial.Serial('COM11', 115200) 

# Get current date and time
current_date = datetime.datetime.now().strftime('%d_%B')
current_time = datetime.datetime.now().strftime('%Hh_%Mm')

# Get user input for supplied voltage and shunt resistance
supplied_voltage = float(input("Enter supplied voltage (V): "))
shunt_resistance = float(input("Enter shunt resistance (kOhm): "))

# Generate filename based on current date, time, supplied voltage, and shunt resistance
filename = f"{current_date}_{current_time}_{supplied_voltage}V_{shunt_resistance}kOhm_log.csv"

# Open CSV file for writing
with open(filename, 'w', newline='') as csvfile:
    data_writer = csv.writer(csvfile)
    data_writer.writerow(['Microseconds', 'Value'])  # Write header
    
    try:
        print(f"Logging data to {filename}...")
        print(f"Press CTRL+C to stop")
        
        while True:
            # Read current time as raw binary data (4 bytes)
            currentTime_bytes = ser.read(4)
            currentTime = struct.unpack('<L', currentTime_bytes)[0]  # Little-endian, unsigned long
            
            # Read analog value as raw binary data (2 bytes)
            value_bytes = ser.read(2)
            value = struct.unpack('<H', value_bytes)[0]  # Little-endian, unsigned short
            
            data_writer.writerow([currentTime, value])  # Write data to CSV
            
            # Print values to console
            #print(f"Time: {currentTime} us, Value: {value}")
            
    except KeyboardInterrupt:
        ser.close()  # Close serial connection
        print("Logging stopped.")
