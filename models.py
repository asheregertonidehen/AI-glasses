import cv2
from PIL import Image
from pytesseract import pytesseract
import pyttsx3
import sys

pytesseract.tesseract_cmd = r"/opt/homebrew/bin/tesseract"
engine = pyttsx3.init()
camera = cv2.VideoCapture(0)

#functions that contain the model information
def ObjectDmodel():
    pass
def FaceDmodel():
    pass
def OCRmodel():
    while True:
        ret, frame = camera.read()
        if not ret:
            break

        # Convert frame (BGR) to RGB for PIL
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        pil_img = Image.fromarray(rgb)

        # OCR on the current frame
        text = pytesseract.image_to_string(pil_img).strip()
        print("\033c", end="")  # Clear terminal for real-time effect
        print(text)

        # Read aloud the text when s(for speak) is pressed
        if text and cv2.waitKey(1) & 0xFF == ord('s'):
            engine.say(text)
            engine.runAndWait()

        # Show the frame
        cv2.imshow('Text detection', frame)

        # Exit on 'z'
        if cv2.waitKey(1) & 0xFF == ord('z'):
            break

#user mode selection
mode = sys.argv[1]
input = sys.argv
if len(input)> 2:
    sys.exit("**too many arguments** type in mode in commandline:\n'OCR' (Text detection)\n'FaceD' (Face detection)\n'ObjectD' (Object detection)")
if mode == "OCR":
    print("staring OCR model...")
    OCRmodel()
if mode == "ObjectD":
    print("staring object detection model...")
    ObjectDmodel()
if mode == "FaceD":
    print("staring face detection model...")
    FaceDmodel()
else:
    sys.exit("**Input a valid mode**\n type in mode in commandline:\n'OCR' (Text detection)\n'FaceD' (Face detection)\n'ObjectD' (Object detection)")


camera.release()
cv2.destroyAllWindows()