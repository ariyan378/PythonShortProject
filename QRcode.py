import qrcode as qr
import PIL
img = qr.make("https://github.com/ariyan378")
img.save("github_ariyan.png")
print(PIL.__version__)