import qrcode
from PIL import Image

img = qrcode.make("https://zdaly.com")
img.save("zdaly.png")