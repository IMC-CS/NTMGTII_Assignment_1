from checksum import calculate_checksum16

def test_checksum16():
    example_bytes = bytearray(b'\x10\x6f\xff\xa4')
    checksum = calculate_checksum16(example_bytes)
    assert checksum == int.from_bytes(b'\xef\xeb', 'little')

    example_bytes = bytearray(b'\x10\x6f\xff\xa4\x10\x6f\xff\xa4')
    checksum = calculate_checksum16(example_bytes)
    assert checksum == int.from_bytes(b'\xdf\xd7', 'little')

    example_bytes = bytearray(b'\x10\x6f\xff\xa4\x10\x00\xff\xff\xa0')
    checksum = calculate_checksum16(example_bytes)
    assert checksum == int.from_bytes(b'\xdf\xeb', 'little')

    example_bytes = bytearray(b'\xff\xff\xff\x00\xff')
    checksum = calculate_checksum16(example_bytes)
    assert checksum == int.from_bytes(b'\x00\xff', 'little')
