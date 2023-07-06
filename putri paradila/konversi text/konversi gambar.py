from PIL import Image

def preprocess_image(image_path):
    # Load image and convert it to grayscale
    image = Image.open(image_path).convert('L')

    # Resize image to a smaller size if needed
    # image = image.resize((new_width, new_height))

    # Flatten the grayscale image into a 1D array of pixel values
    pixels = list(image.getdata())

    return pixels

def compress_rle(pixels):
    compressed_pixels = []
    count = 1
    for i in range(1, len(pixels)):
        if pixels[i] == pixels[i - 1]:
            count += 1
        else:
            compressed_pixels.append(pixels[i - 1])
            compressed_pixels.append(count)
            count = 1
    compressed_pixels.append(pixels[-1])
    compressed_pixels.append(count)
    return compressed_pixels

# Praproses gambar pegunungan
image_path = "pegunungan.jpg"
pixels = preprocess_image(image_path)

# Kompresi gambar dengan algoritma RLE
compressed_pixels = compress_rle(pixels)

# Menyimpan hasil kompresi dalam file teks
output_file = "compressed_image.txt"
with open(output_file, "w") as file:
    for pixel in compressed_pixels:
        file.write(str(pixel) + "\n")

print("Compression completed. Compressed pixels saved in", output_file)
image = Image.open(image_path)
output_path = "Hasil.jpg"
image.save(output_path)
image.show(output_path)