from PIL import Image, ImageEnhance

gambar = Image.open("logo.jpg")

enhancer = ImageEnhance.Brightness(gambar)
gambar_terang = enhancer.enhance(0.5) 

gambar_terang.save("logo_gelap.jpg")