import asyncio
import struct
import numpy as np
import datetime
import time
import sys
import os
import socket
import json

 # Define the UDP address and port for PlotJuggler
UDP_IP = "127.0.0.1"
UDP_PORT = 9870
# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Replace these with your actual BLE device address and UUIDs
DEVICE_ADDRESS = "0C:EF:F6:FB:28:B7"  # Replace with your device's address
SERVICE_UUID = "1a4e06aa-a600-4094-a0bb-698edc027190"  # Sensor Bolt Service UUID
CHARACTERISTIC_UUIDS = [    
    "00002a6e-0000-1000-8000-00805f9b34fb",  # Temperature  UUID
    "34850bc9-95e5-4701-956c-656ce1afdc66",  # Strain 1 UUID
    "ce645fc0-9d46-42ef-a89c-9699c0121c65",  # Strain 2 UUID
    "1062d25e-b825-457d-807b-9b02e2f5cb80",  # Strain 3 UUID
    "0f88a878-8b02-44cb-8fad-a317f24edaf9"   # Combined UUID
]


# Define a structured numpy array with a timestamp field
data_type = np.dtype([('strain_1', 'f4'), 
                      ('strain_2', 'f4'), 
                      ('strain_3', 'f4'), 
                      ('temp', 'f4'),
                      ('timestamp', 'datetime64[us]')])  # Timestamp formatted as string

# Global NumPy array for storing data
global_data = np.empty((0,), dtype=data_type)

def ieee754_hex_to_float(hex_value):
    int_value = int(hex_value, 16)
    float_value = struct.unpack('>f', struct.pack('@I', int_value))[0]
    return float_value

def sint16_hex_to_int(hex_value):
    int_value = int(hex_value, 16)
    signed_int_value = struct.unpack('>h', struct.pack('@H', int_value))[0]
    return signed_int_value
    

def parse_data_to_numpy(strain_1, strain_2, strain_3, temp):

    #strain_1 / _2 / _3 -> float
    #temp -> int
    

    global global_data

##    strain_1_hex = data[:8]
##    strain_2_hex = data[8:16]
##    strain_3_hex = data[16:24]
##    temp_hex = data[24:28]
##    
##    
##    strain_1 = ieee754_hex_to_float(strain_1_hex)
##    strain_2 = ieee754_hex_to_float(strain_2_hex)
##    strain_3 = ieee754_hex_to_float(strain_3_hex)
##    
##    temp = sint16_hex_to_int(temp_hex) / 100
    
    # Add timestamp
    timestamp = datetime.datetime.now()

    # Create a structured NumPy array
    parsed_data = np.array((strain_1, strain_2, strain_3, temp, timestamp), dtype=data_type)    
    

    if temp > -40 and temp < 125:  # Filter out invalid temperature values   
        # Append to global NumPy array
        global_data = np.append(global_data, parsed_data)        
        # Convert the parsed data to a JSON string and send it over UDP
        data_dict = {
            "timestamp": timestamp.timestamp(),
            "strain_1": strain_1,
            "strain_2": strain_2,
            "strain_3": strain_3,
            "temp": temp        
        }    
        data_json = json.dumps(data_dict)
        sock.sendto(data_json.encode(), (UDP_IP, UDP_PORT))
                   
    return parsed_data

def save_numpy_data_to_file():
    """ Save global NumPy array to a file """
    global global_data

    if global_data.size > 0:
        save_path = os.path.join(os.path.dirname(__file__), "sensor_dump_test.npy")
        np.save(save_path, global_data)  # Save as binary NumPy file
        print(f"Saved {global_data.shape[0]} entries to .npy")
        print(os.getcwd())

def main():
    global global_data
    for i in range (100):
        parse_data_to_numpy(float(i), float(i), float(i), int(i+10))
        time.sleep(0.01)

    save_numpy_data_to_file()
    print(global_data)

if __name__ == "__main__":
    main()
