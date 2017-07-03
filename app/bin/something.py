import PIL
from PIL import ImageGrab

img = ImageGrab.grab()
print ("the size of the Image is: ")
print(img.format, img.size, img.mode)
img.show()
