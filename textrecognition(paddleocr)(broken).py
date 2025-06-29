from paddleocr import PaddleOCR
import cv2
from matplotlib import pyplot as plt
import random

image_path_random = str(f"test{str(random.randint(2,1000000))}.jpg")
ocr = PaddleOCR(use_angle_cls=True, lang='en') #called image of the 
image_path = 'test-image.png'

camera=cv2.VideoCapture(0)

while True:
    _, frame = camera.read()
    cv2.imshow('Text detection', frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):
        cv2.imwrite(image_path_random, frame)
        break
    elif key == ord('z'):
        break
camera.release()
cv2.destroyAllWindows()
camera.release()


cv2.destroyAllWindows()
#plt.figure()
#plt.imshow(img)
#plt.show()
result = ocr.ocr(image_path_random)
if result and len(result[0]) > 0:
    for line in result[0]:
        print(line[1][0])
else:
    print("No text detected.")
#[0][1][1][0]