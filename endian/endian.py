# litle endian
def to_little_endian(word):
    # Tentukan panjang byte yang sesuai dengan panjang word
    byte_length = (word.bit_length() + 7) // 8  # Menentukan panjang byte secara dinamis
    little_endian = word.to_bytes(byte_length, byteorder='big')[::-1]  # Balik urutannya
    return little_endian.hex()  # Mengembalikan dalam bentuk heksadesimal

word = 0x6a74696c73  # Nilai lebih besar dari 16-bit
result = to_little_endian(word)
print(result)

# big endian
def to_big_endian(word):
    # Tentukan panjang byte yang sesuai dengan panjang word
    byte_length = (word.bit_length() + 7) // 8  # Menentukan panjang byte secara dinamis
    big_endian = word.to_bytes(byte_length, byteorder='big')  # Big-endian (default)
    return big_endian.hex()  # Mengembalikan dalam bentuk heksadesimal

word = 0x746a766d67  # Nilai lebih besar dari 16-bit
result = to_big_endian(word)
print(result)

