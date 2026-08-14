# Decoding ADS-B messages
# Sample Message: 8D4840D6202CC371C32CE0576098
print()
samp_msg = "8D4840D6202CC371C32CE0576098"
num_bits = len(samp_msg) * 4    # number of bits in binary from hex
bin_msg = format(int(samp_msg, 16), f'0{num_bits}b')    # to binary w/ padding

print(f"Sample Message: {samp_msg}")
print(f"Sample Message in Binary: {bin_msg}")
# print(f"Number of bits: {num_bits}")
print()

DF = int(bin_msg[0:5], 2)    # binary back to decimal w/ slice
ICAO = samp_msg[2:8]    # slice hex string

print(f"DF: {DF}")
print(f'ICAO: {ICAO}')


# # int(text, base) converts string to integer
# print(int("8D", 16)) # 141
# print(int("10001", 2)) # 17

# # bin(number) number to binary string
# print(bin(141)) # 0b10001 (need to slice 0b)

# #  text[start:end] to slice
# print(bin(141)[2:]) # 10001101 (sliced 0b)

# print("DF: ")
# print("ICAO:")

# print(f"DF: {downlink_format}")




