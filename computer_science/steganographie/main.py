import cv2
import time
from steganography import *


image_path = "Hu.bmp"

text = "Victor rend mon quad batard"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

steganographied_image = stegano(image,text)
# cv2.imshow("steganographied_image", steganographied_image)
# cv2.waitKey(0)

hidden_text = get_text_from_steganographied_image(steganographied_image)
print(hidden_text)