import random
import cv2 #gets images from the webcam
from PIL import Image #manipulating images
from pytesseract import pytesseract #OCR tech for reading the words

camera=cv2.VideoCapture(0) # created to represent the came (0 access the webcam)

image_name = str(f"test{str(random.randint(2,1000000))}")

def tesseract():
    path_to_tesseract = r"/opt/homebrew/bin/tesseract"  # Update this path if your tesseract is elsewhere
    ImagePath = "image_name"
    pytesseract.tesseract_cmd=path_to_tesseract
    text=pytesseract.image_to_string(Image.open(ImagePath))
    print(text[:-1])
tesseract()

while True: #read webcam stream untill loop breaks
    _,frame=camera.read() #_, ignores the first return boolean value
    cv2.imshow('Text detection', frame) #reads the image and shows it
    if cv2.waitKey(1)& 0xFF==ord('s'): #if the s key is pressed:
        cv2.imwrite(image_name, frame) #store the image as "test1.jpg"
        tesseract()
    if cv2.waitKey(1)& 0xFF==ord('z'):
        break
camera.release()
cv2.destroyAllWindows()

