import threading

def click_point():
    import time
    import pyautogui
    # Specify the time delay in seconds
    delay = 60 * 2
    # Specify the coordinates of the point to click
    x = 1309
    y = 118
    # Wait for the specified time delay
    time.sleep(delay)
    # Click the specified point
    pyautogui.click(x, y)

def press_random_arrow():
    """Press a random arrow key."""
    import pyautogui
    import time
    import random
    pyautogui.FAILSAFE = True
    arrows = ['up', 'down']
    random_arrow = random.choice(arrows)
    pyautogui.press(random_arrow)

def main():
    try:
        while True:
            # Create threads for each function
            click_thread = threading.Thread(target=click_point)
            arrow_thread = threading.Thread(target=press_random_arrow)

            # Start the threads
            click_thread.start()
            arrow_thread.start()

            # Wait for both threads to finish
            click_thread.join()
            arrow_thread.join()

            time.sleep(5)
    except KeyboardInterrupt:
        print("\nEnded")

if __name__ == "__main__":
    main()