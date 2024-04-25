import pyautogui
import datetime
import time

def take_screenshot_after_delay(delay=30):
    # Sleep for the specified delay
    time.sleep(delay)
    
    # Generate a timestamp for the filename
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"screenshot_{timestamp}.png"
    
    # Take screenshot and save it with the generated filename
    screenshot = pyautogui.screenshot()
    screenshot.save(filename)
    print(f"Screenshot taken and saved as '{filename}'")

if __name__ == "__main__":
    take_screenshot_after_delay()
