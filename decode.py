## Decoding ADS-B messages

# Sample Message: 8D4840D6202CC371C32CE0576098
print()
msg_samp = "8D4840D6202CC371C32CE0576098"
num_bits = len(msg_samp) * 4                            # number of bits in binary from hex
msg_bin = format(int(msg_samp, 16), f'0{num_bits}b')    # to binary w/ padding

print(f"Sample Message: {msg_samp}")
# print(f"Sample Message in Binary: {msg_bin}")
# print(f"Number of bits: {num_bits}")
print()

DF = int(msg_bin[0:5], 2)   # binary back to decimal w/ slice
ICAO = msg_samp[2:8]        # slice hex string

print(f"DF: {DF}")
print(f'ICAO: {ICAO}')
print()

#CRC
gen = 0xFFF409                                  # Mode S generator polynomial
msg_bin_88 = [int(b) for b in msg_bin[0:88]]    # first 88 bits CRC protects as ints
reg = msg_bin_88 + [0] * 24  

# print(f"before: {reg}")                   # 24 zero bits added as space
# stamp 24 bits to the right of i and XOR it with the gen
for i in range(88):
    if reg[i] == 1:                         # pass through each bit seeing if "1", if "0" goes to next i                             # if bit is 1, XOR with generator
        for j in range(24):                 # runs when bit is 1
            gen_bit = (gen >> (23 - j)) & 1 # which bit lines up
            reg[i + 1 + j] ^= gen_bit

# print(f"after: {reg}") 
computed_crc_str = ''.join(str(b) for b in reg[88:112])
raw_crc_str = msg_bin[88:112]

print(f"Computed CRC: {computed_crc_str}")
print(f"Raw/received CRC: {raw_crc_str}")
print(f"CRC Match: {computed_crc_str == raw_crc_str}")

