import PIL
import qrcode
from PIL import Image
import qrcode.constants 

qr =  qrcode.QRCode(version = 1 ,
                    error_correction = qrcode.constants.ERROR_CORRECT_H,
                    box_size= 10 , border = 4, )

qr.add_data("http://127.0.0.1:5500/portfolio%20project/index.html")
qr.make("bool fit = true")
img = qr.make_image(fill_color = "black" , back_color="white")
img.save("Ariyan_Linkdin.png")
print(Image.__version__)
print(PIL.__version__)