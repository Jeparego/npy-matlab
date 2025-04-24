import struct

def ieee754_hex_to_float(hex_value):
    int_value = int(hex_value, 16)
    float_value = struct.unpack('>f', struct.pack('@I', int_value))[0]
    return float_value

def sint16_hex_to_int(hex_value):
    int_value = int(hex_value, 16)
    signed_int_value = struct.unpack('>h', struct.pack('@H', int_value))[0]
    return signed_int_value


def main():
    print(ieee754_hex_to_float('0A'))

main()    
