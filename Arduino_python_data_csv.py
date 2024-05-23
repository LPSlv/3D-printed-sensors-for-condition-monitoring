import serial
import csv
import time
import struct

arduino = serial.Serial('COM11', 115200)

# Dati faila nosaukumam
current_date = time.strftime('%d_%B')
current_time = time.strftime('%Hh_%Mm')
voltage = float(input("Voltage: (V): "))
shunt_resistance = float(input("Shunt resistor (kOhm): "))
filename = f"{current_date}_{current_time}_{voltage}V_{shunt_resistance}kOhm_log.csv"

buffer_size = 100


with open(filename, 'w', newline='') as file:
    data_writer = csv.writer(file)
    
    # Faila galvene
    data_writer.writerow(['Microseconds', 'Value'])
    
    buffer = []

    try:
        print(f"Filename: {filename}...")
        print(f"CTRL+C to stop")
        
        start_time_ns = time.perf_counter_ns()

        while True:
            # Nolasa 2 baitus
            data = arduino.read(2)
            try:
                # Little-endian, unsigned short formats
                sensor_value = struct.unpack('<H', data)[0]  
                
                # Laiks, kas pagajis kops merijuma saksanas
                elapsed_time_ns = time.perf_counter_ns() - start_time_ns
                elapsed_time_us = elapsed_time_ns // 1000
                
                buffer.append([elapsed_time_us, sensor_value])

                # Ja buferis ir pilns, ieraksta datus faila
                if len(buffer) >= buffer_size:
                    data_writer.writerows(buffer)
                    buffer = []

                print(f"Microseconds: {elapsed_time_us}, Value: {sensor_value}")
                
            except KeyboardInterrupt:
                if buffer:
                    data_writer.writerows(buffer)
                arduino.close()
                print("Stopped")
                break
    except serial.SerialException as e:
        print(f"Serial error: {e}")
