# Example checksum calculation

def calculate_checksum8(data: bytes) -> bytes:
    """
    Calculates a checksum from an array of bytes (8 bits).
    """
    checksum = 0
    carry_sum = 0
    for b in data:
        checksum += b
        carry = (checksum & 0xFF00) >> 8  # checksum = 0x0100 & 0xFF00 = 0x0100 >> 8 -> 0x0001
        carry_sum += carry
        checksum = checksum & 0x00FF  # 0x0156 -> 0x0056

    checksum += carry_sum
    carry = (checksum & 0xFF00) >> 8
    checksum += carry
    checksum = checksum ^ 0xFF  # NEGATE the result -> XOR with 0xFF


    # XOR Truth table
    # 0 0 -> 0
    # 0 1 -> 1 (negates 0)
    # 1 0 -> 1
    # 1 1 -> 0 (negates 1)

    return checksum

def calculate_checksum16(data: bytes) -> int:
    """
    Calculates a 16-bit checksum (little-endian) following
    the same algorithmic structure as calculate_checksum8.
    """
    checksum = 0
    carry_sum = 0

    for i in range(0, len(data), 2):
        if i + 1 < len(data):
            word = data[i] | (data[i + 1] << 8)  # little-endian
        else:
            word = data[i] | (0x00 << 8) 
        checksum += word
        carry = (checksum & 0xFFFF0000) >> 16
        carry_sum += carry
        checksum &= 0xFFFF

    checksum += carry_sum
    carry = (checksum & 0xFFFF0000) >> 16
    checksum += carry
    checksum &= 0xFFFF
    checksum ^= 0xFFFF

    return checksum


# Example usage
example_bytes = bytearray(b'\x10\x6f\xff\xa4')
checksum = calculate_checksum8(example_bytes)
print(f'Checksum of {example_bytes} is 0x{checksum:02X}')  # Print as 2-digit hex

example_bytes.append(checksum)

verify = calculate_checksum8(example_bytes)
print(f'Data frame = {example_bytes}, result of verification = 0x{verify:02X}')

