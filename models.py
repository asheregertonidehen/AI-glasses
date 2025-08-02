import cv2
from PIL import Image
from pytesseract import pytesseract
import pyttsx3
import sys

pytesseract.tesseract_cmd = r"/opt/homebrew/bin/tesseract"
engine = pyttsx3.init()
camera = cv2.VideoCapture(0)

#####- Model Functions Area -#####

def voiceMode():
    pass
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

        # Read aloud the text when S (for speak) is pressed
        if text and cv2.waitKey(1) & 0xFF == ord('s'):
            engine.say(text)
            engine.runAndWait()

        # Show the frame
        cv2.imshow('Text detection', frame)

        # Exit on 'E'
        if cv2.waitKey(1) & 0xFF == ord('e'):
            break

#####- Command Line Selection Area -#####
input = sys.argv
#user model selection (OCR, ObjecDetection, FaceDetection)
model = sys.argv[1]
def selectModel():
    if model == "OCR":
        print("staring OCR model...")
        OCRmodel()
    if model == "ObjectD":
        print("staring object detection model...")
        ObjectDmodel()
    if model == "FaceD":
        print("staring face detection model...")
        FaceDmodel()
    else:
        sys.exit("**Input a valid mode**\n type in mode in commandline:\n'OCR' (Text detection)\n'FaceD' (Face detection)\n'ObjectD' (Object detection)")

#user mode selection (Regular, Voice activation)
mode = sys.argv[2]
if len(input)> 3:
    sys.exit("**too many arguments** type in mode in commandline:\n'OCR' (Text detection)\n'FaceD' (Face detection)\n'ObjectD' (Object detection)")
if len(input) == 2:
    print("Mode selection regular")
    selectModel()
if len(input) == 3 and mode == "voice":
    print("Mode selection voice")
    voiceMode()
    selectModel()



camera.release()
cv2.destroyAllWindows()