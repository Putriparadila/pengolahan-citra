def compress_rle(data):
    compressed_data = ""
    count = 1
    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            count += 1
        else:
            compressed_data += data[i - 1] + str(count)
            count = 1
    compressed_data += data[-1] + str(count)
    return compressed_data

data = "Putriii Paradilaaa"
compressed_data = compress_rle(data)
print("Compressed Data:", compressed_data)
