import os 
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

import cv2
from cvzone.HandTrackingModule import HandDetector

class Button:
    def __init__(self, pos, width, height, value):
        self.pos = pos
        self.width = width
        self.height = height
        self.value = value

                        
    def draw(self, img):
        cv2.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height), 
                      (132, 164, 196), cv2.FILLED)
        cv2.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height), 
                      (51, 64, 92), 3)
        cv2.putText(img, self.value, (self.pos[0] + 40, self.pos[1] + 50), cv2.FONT_HERSHEY_COMPLEX, 
                      1.25,(50, 50, 50), 3)
        

    def checkClick(self, x, y):
        if self.pos[0] < x < self.pos[0] + self.width and \
           self.pos[1] < y < self.pos[1] + self.height:
            cv2.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height), 
                          (255, 255, 255), cv2.FILLED)
            cv2.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height), 
                          (50, 50, 50), 3)
            cv2.putText(img, self.value, (self.pos[0] + 20, self.pos[1] + 60), cv2.FONT_HERSHEY_COMPLEX,
                        2, (0, 0, 0), 3)
            return True
        else:
            return False
        

cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # Width
cap.set(4, 720)   # Height

detector = HandDetector(detectionCon=0.8, maxHands=1)

# Creating buttons
buttonListValues = [['C', '7', '8', '9','='],
                    ['+', '4', '5', '6','*'],
                    ['-', '1', '2', '3','/'],
                    ['%', '0', '00', '.','//']]


buttonList = []
for y in range(4):  # Rows
    for x in range(5):  # Columns
        xpos = x * 100 + 650
        ypos = y * 100 + 150
        buttonList.append(Button((xpos, ypos), 100, 100, buttonListValues[y][x]))


calculation = ''
delay_count = 0

while True:
    # Get image from webcam
    success, img = cap.read()
    img = cv2.flip(img, 1)

    # Hand detection
    hands, img = detector.findHands(img, flipType=False)

    # Draw all buttons
    cv2.rectangle(img, (650, 50), (650 + 500, 50 + 100), (225, 225, 225), cv2.FILLED)
    cv2.rectangle(img, (650, 50), (650 + 500, 50 + 100), (50, 50, 50), 3)
    for button in buttonList:
        button.draw(img)


    # Check for hand
    if hands:
        lmList = hands[0]['lmList']
        index_tip = lmList[8][0:2]  # (x, y) for index finger tip
        middle_tip = lmList[12][0:2]  # (x, y) for middle finger tip

        length, _, img = detector.findDistance(index_tip, middle_tip, img)
        x, y = index_tip  # Coordinates of index finger tip

        if length < 60:
            for i, button in enumerate(buttonList):
                if button.checkClick(x, y) and delay_count == 0:
                    row = int(i // 5)
                    column = int(i % 5)
                    value = buttonListValues[row][column]
                    if value == '=':
                        try:
                            calculation = str(eval(calculation))
                        except:
                            calculation = 'Error'
                    elif value == 'C':
                        calculation = ''
                    else:
                        if len(calculation) < 14:
                            calculation += value
                    delay_count = 1


    # Avoid duplicates 
    if delay_count != 0:
        delay_count += 1
        if delay_count > 10:
            delay_count = 0


    # Display the equation/result
    cv2.putText(img, calculation, (690, 120), cv2.FONT_HERSHEY_PLAIN, 3, (50, 50, 50), 3)

    # Display the image
    cv2.imshow("Image", img)
    key = cv2.waitKey(1)

    if key == ord('c'):
        calculation = ''
    if key == ord('f'):
        break
