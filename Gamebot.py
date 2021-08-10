"""
This is an attempted bot for Clash of Clans
It will ideally keep cycling through bases until an optimal resource allocation has been found.
It uses BlueStacks to host the game.
"""
from PIL import Image
import pytesseract
import cv2
import numpy as np
import pyautogui
import random
import time

# Location of the top 3 stats to analyze
TOP_LEFT = (458, 159)
BOTTOM_RIGHT = (588, 313)
REGION = (458, 159, 150, 150)

# Location of next button.
NEXT_BUTTON_TOP_X = 1869
NEXT_BUTTON_BOTTOM_X = 2124
NEXT_BUTTON_TOP_Y = 698
NEXT_BUTTON_BOTTOM_Y = 805

randx = random.randrange(NEXT_BUTTON_TOP_X, NEXT_BUTTON_BOTTOM_X)
randy = random.randrange(NEXT_BUTTON_TOP_Y, NEXT_BUTTON_BOTTOM_Y)
print(f'Randx: {randx}, Randy: {randy}')

# Pass Criteria
GOLD = 300000
ELIXIR = 300000
OIL = 10000
unviable = True

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\User\AppData\Local\Programs\Tesseract-OCR\tesseract'

# get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def get_blurred(image):
    return cv2.GaussianBlur(image, (5, 5), 0)


def get_nums(input_string):
    broken_down_list = [char for char in input_string]
    num_only = '0'
    for char in broken_down_list:
        if char.isnumeric():
            num_only = num_only + char

    result = int(num_only)
    return result


def check_vars(gold=0, elixir=0, oil=0):
    if gold > GOLD or elixir > ELIXIR or oil > OIL:
        return True
    else:
        return False


game_round = 0

def increase_round():
    return game_round + 1


while unviable:
    # screenshot
    int_sleep = random.randrange(3)
    time.sleep(int_sleep)
    screenshot = pyautogui.screenshot(region=REGION)
    screenshot.save('newtest.jpg')  ## This is used for testing - to see what the output is
    time.sleep(0.5)
    location = "C:/Users/User/PycharmProjects/GameBot/newtest.jpg"
    img = cv2.imread(location)
    img = get_grayscale(img)
    img = get_blurred(img)

    # Analyze
    text = pytesseract.image_to_string(img)
    print(f"Round {game_round}\nText: {text}")
    try:
        img_gold, img_elixir, *img_oil = text.split('\n')
        img_gold = get_nums(img_gold)
        img_elixir = get_nums(img_elixir)
        img_oil = ''.join(img_oil)
        img_oil = get_nums(img_oil)
    except ValueError:
        split_text = text.split('\n')
        options = [get_nums(x) for x in split_text]
        if len(options) == 1:
            img_gold = options[0]
        elif len(options) == 2:
            img_gold = options[0]
            img_elixir = options[1]
        else:
            img_gold = options[0]
            img_elixir = options[1]
            img_oil = options[2:]

    print(f'Post Processed text Gold: {img_gold}, Elixir: {img_elixir}, Oil: {img_oil}')

    # print(img_gold, img_elixir, img_oil)
    # cv2.imshow('Image', img)

    if check_vars(img_gold, img_elixir, img_oil):
        # Make a notification of some sort
        print("criteria met")
        break
    random_time_ms = random.randrange(1, 100) / 100
    random_time_sec = random.randrange(0, 3)
    joined_time = random_time_sec + random_time_ms
    time.sleep(joined_time)
    pyautogui.moveTo(randx, randy, duration=0.52)
    pyautogui.click()
    game_round = increase_round()
    if game_round >4:
        unviable = False

    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


# # location = "C:/Users/User/PycharmProjects/GameBot/cocloot.jpg"
# # location = "C:/Users/User/PycharmProjects/GameBot/coctest2.jpg"
# location = "C:/Users/User/PycharmProjects/GameBot/Screenshot_2.jpg"
#
# img = cv2.imread(location)
# img = get_grayscale(img)
# img = get_blurred(img)
#
# text = pytesseract.image_to_string(img)
# print("Text: ", text)
#
# cv2.imshow('Image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#



# img = pyautogui.screenshot(region=(0, 0, 300, 300))
# grag = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# # img.save("TestShot.jpg")
# filename = 'test.png'
# cv2.imwrite(filename, grag)
#
# # SCREEN_SIZE = (2560, 1080)
# #
# # fourcc = cv2.VideoWriter_fourcc(*"XVID")
# # # create the video write object
# # out = cv2.VideoWriter("output.avi", fourcc, 20.0, (SCREEN_SIZE))
# #
# #
# # for i in range(50):
# #     # make a screenshot
# #     img = pyautogui.screenshot(region=(0, 0, 300, 300))
# #     frame = np.array(img)
# #     frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
# #     # write the frame
# #     out.write(frame)
# #     # show the frame
# #     cv2.imshow("screenshot", frame)
# #
# # cv2.destroyAllWindows()
# # out.release()

"""
Steps
1. Take screenshot of numbers
2. Analyze screenshot and determine numbers
3. Determine whether numbers meet criteria
    3.a) If numbers meet criteria, stop/pop up
    3.b) If numbers do not meet criteria, place cursor over next button. Click. Loop again. 
"""

# # Outline the range of the box, then move the mouse around minimally inside it.
# options = ['easeInOutQuad']
# currentMouseX, currentMouseY = pyautogui.position()
# print(currentMouseX, currentMouseY)




# pyautogui.moveTo(4105, 873, duration=0.51, tween=pyautogui.easeInOutQuad)
# pyautogui.moveTo(2657, 302)
# for i in range(10):
#     pyautogui.click() 1869 698