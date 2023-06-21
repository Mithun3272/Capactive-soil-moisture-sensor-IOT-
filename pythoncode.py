import serial
import time

# Set up the serial connection
ser = serial.Serial('COM4', 9600)  # Replace 'COM3' with the appropriate port for your Arduino
time.sleep(2)  # Wait for the connection to establish

# Define the moisture sensor thresholds
wet = 210
dry = 510

while True:
    # Read the moisture value from the Arduino
    value = int(ser.readline().strip().decode('utf-8'))
    
    # Map the moisture value to a percentage
    percentage = 100 - ((value - wet) / (dry - wet)) * 100
    percentage = max(0, min(100, percentage))  # Clamp the percentage between 0 and 100
    
    # Display the moisture value on the console
    print(f"Moisture value: {value}")
    print(f"Percentage: {percentage}%")
