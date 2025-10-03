# Example checksum calculation

def calculate_checksum8(bytes: bytes) -> bytes:
    """
    Calculates a checksum from an array of bytes (8 bits).
    """
    checksum = 0
    carry_sum = 0
    for b in bytes:
        checksum += b
        carry = (checksum & 0xFF00) >> 8 # checksum = 0x0100 & 0xFF00 = 0x0100 >> 8 -> 0x0001
        carry_sum += carry 
        checksum = checksum & 0x00FF # 0x0156 -> 0x0056
    
    checksum += carry_sum
    carry = (checksum & 0xFF00) >> 8
    checksum += carry
    checksum = checksum ^ 0xFF # NEGATE the result -> XOR with 0xFF

    # XOR Truth table
    # 0 0 -> 0
    # 0 1 -> 1 (negates 0)
    # 1 0 -> 1
    # 1 1 -> 0 (negates 1)

    return checksum


def calculate_checksum16(data: bytes) -> int:
    """
    Calculates a 16-bit one's complement checksum from a byte array.
    Each iteration processes two bytes as one 16-bit word.
    """
    checksum = 0
    length = len(data)

    # 如果字节数是奇数，最后一个字节需要补 0
    if length % 2 == 1:
        data += b"\x00"

    # 每次取 2 个字节，组成一个 16-bit word
    for i in range(0, len(data), 2):
        word = (data[i] << 8) + data[i+1]  # 高位在前，低位在后
        checksum += word
        checksum = (checksum & 0xFFFF) + (checksum >> 16)  # 加上溢出的进位

    # 最后取反
    checksum = checksum ^ 0xFFFF
    return checksum



example_bytes = bytearray(b'\x10\x6f\xff\xa4')
checksum = calculate_checksum8(example_bytes)
print(f'Checksum of {example_bytes} is 0x{checksum:X}') # :X modifies the format to print in hexadecimal

example_bytes.append(checksum)

verify = calculate_checksum8(example_bytes)
print(f'Data frame = {example_bytes}, result of verification = 0x{verify:X}')



