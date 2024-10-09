import pyautogui
import time
from PIL import ImageGrab

# Get the size of the primary monitor.
screenWidth, screenHeight = pyautogui.size()

# Click on start menu (adjust the coordinates as per your screen resolution)
pyautogui.moveTo(620, 1055)
pyautogui.click()

# Type chrome and enter
pyautogui.write('chrome', interval=.15)
pyautogui.press('enter')

# Type the website and enter
time.sleep(1)
pyautogui.write('https://elgoog.im/t-rex/')
pyautogui.press('enter')

# Press F11 to go full screen and start the game with space
time.sleep(7)
pyautogui.press('f11')
time.sleep(1)
pyautogui.press('space')


def is_obstacle_in_area(pixel, white_code):
    for x in range(20, 60):  # Check a range of x-coordinates
        for y in range(10, 20):  # Check a range of y-coordinates
            if px[x, y] != white_color:
                return True
    return False


# Set initial x position for obstacle detection
x_position = 215  # Move the detection closer to the dino
white_color = (255, 255, 255)

# Main loop to detect obstacles and jump
try:
    while True:
        # Capture part of the screen where obstacles appear (adjust bbox values)
        screen = ImageGrab.grab(bbox=(x_position, 564, x_position + 210, 623))
        px = screen.load()

        # Use the function in your loop
        if is_obstacle_in_area(px, white_color):
            pyautogui.press('space')

        # Increment x position based on game speed (tweak this if needed)
        x_position += 1  # Keep small increments for smoother adjustment
        time.sleep(0.05)  # Adding a short delay for smoother detection

except KeyboardInterrupt:
    print("Game interrupted.")
