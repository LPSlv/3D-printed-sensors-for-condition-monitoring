
import serial
import time
import signal

# Set initial parameters
log_count = 1
Baudrate = 9600

# Get user input for serial port and sensor parameters
COMport = input('[Windows - COMxx or Linux - /dev/ttyUSBx]\nEnter Serial Port Number ->')
suppliedV = input('Enter supplied sensor voltage (V) ->')
shuntR = input('Enter shunt resistor value (kOhm) ->')

# Print selected port and parameters
print('\nPort Selected ->', COMport.upper())
print('\nSensor supplied voltage (V) ->', suppliedV)
print('\nShunt resistor value (kOhm) ->', shuntR)
print('Baud Rate ->', Baudrate)

# Get current local time
current_local_time = time.localtime()
filename = time.strftime("%d_%B_%Hh_%Mm_", current_local_time) + suppliedV + 'V_' + shuntR + 'kOhm_' + 'log.csv'
print(f'Created Log File -> {filename}')

# Create a csv File header
with open(filename, 'w+') as csvFile:
    csvFile.write('Num,Micros,Value\n')

# Open serial connection
SerialObj = serial.Serial(COMport, Baudrate)

print('3 sec Delay for Arduino Reset')
time.sleep(3)

# Send symbol '$' to reset timer on Arduino
SerialObj.write(b'$')

# Signal Handler for CTRL+C
def SignalHandler_SIGINT(SignalNumber, Frame):
    print ('CTR+C Pressed, Signal Caught')
    global sentry
    sentry = False
    print ('sentry = ', sentry)

signal.signal(signal.SIGINT, SignalHandler_SIGINT)

# Flag for program execution
sentry = True

# Counter for samples processed
sample_count = 0

# Main loop for data logging
while sentry:
    ReceivedString = SerialObj.readline()
    ReceivedString = str(ReceivedString, 'utf-8').rstrip()  # Remove trailing newline character
    tempSplitList = ReceivedString.split('-')

    #if len(tempSplitList) >= 2:
    # Skip writing to file for the first 1000 samples
    if sample_count >= 1000:
        log_file_text1 = str(log_count) + ',' + tempSplitList[0] + ',' + tempSplitList[1]
            
        # Write to the CSV file only if there are enough elements in tempSplitList
        with open(filename, 'a') as LogFileObj:
            LogFileObj.write(log_file_text1 + '\n')  # Add newline character here

        print(log_file_text1 + '\n')
        log_count += 1

    # Increment sample count
    sample_count += 1

SerialObj.close()

print('Data logging stopped')
print('====================================')
