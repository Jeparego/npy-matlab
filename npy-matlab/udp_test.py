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

# Define a structured numpy array with a timestamp field
data_type = np.dtype([('strain_1', 'f4'), 
                      ('strain_2', 'f4'), 
                      ('strain_3', 'f4'), 
                      ('temp', 'f4'),
                      ('timestamp', 'datetime64[us]')])  # Timestamp formatted as string

# Global NumPy array for storing data
global_data = np.empty((0,), dtype=data_type)

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
    

    if temp > -40:  # Filter out invalid temperature values   
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



def main():
    global global_data
    i = 0;
    while True:
        parse_data_to_numpy(float(i), float(i), float(i), int(i+10))
        time.sleep(0.1)
        i = i+1

    print(global_data)

if __name__ == "__main__":
    main()
