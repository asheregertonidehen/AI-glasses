import cv2
from PIL import Image
from pytesseract import pytesseract
import pyttsx3

pytesseract.tesseract_cmd = r"/opt/homebrew/bin/tesseract"

engine = pyttsx3.init()
camera = cv2.VideoCapture(0)

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

camera.release()
cv2.destroyAllWindows()