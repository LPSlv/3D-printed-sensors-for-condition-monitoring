import serial
import csv
import time
import struct

ser = serial.Serial('COM11', 115200)

current_date = time.strftime('%d_%B')
current_time = time.strftime('%Hh_%Mm')

supplied_voltage = float(input("Enter supplied voltage (V): "))
shunt_resistance = float(input("Enter shunt resistance (kOhm): "))

filename = f"{current_date}_{current_time}_{supplied_voltage}V_{shunt_resistance}kOhm_log.csv"

with open(filename, 'w', newline='') as csvfile:
    data_writer = csv.writer(csvfile)
    data_writer.writerow(['Microseconds', 'Value'])
    
    try:
        print(f"Logging data to {filename}...")
        print(f"Press CTRL+C to stop")
        
        start_time_ns = time.perf_counter_ns()  # Start time in nanoseconds
        
        while True:
            # Read 2 bytes (16 bits)
            data = ser.read(2)
            
            try:
                # Unpack binary data to integer
                sensorValue = struct.unpack('<H', data)[0]  # Little-endian, unsigned short
                
                elapsed_time_ns = time.perf_counter_ns() - start_time_ns
                elapsed_time_us = elapsed_time_ns // 1000  # Convert nanoseconds to microseconds
                
                data_writer.writerow([elapsed_time_us, sensorValue])
                
                print(f"Microseconds: {elapsed_time_us}, Value: {sensorValue}")
                
            except ValueError:
                print(f"Invalid data: {data}")
                
    except KeyboardInterrupt:
        ser.close()
        print("Logging stopped.")
    except serial.SerialException as e:
        print(f"Serial error: {e}")
