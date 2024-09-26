import subprocess
import pyautogui
import time


def open_browser(url):
    # Command to open Chrome in a new window with the specified URL
    chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    subprocess.Popen([chrome_path, '--new-window', url])
    time.sleep(0.5)  # Wait for the browser to open

def move_window_quarter(position):

    if position == "top_left":
        pyautogui.hotkey('win', 'left')
        time.sleep(0.4)
        pyautogui.hotkey('win', 'up')
    elif position == "top_right":
        pyautogui.hotkey('win', 'right')
        time.sleep(0.4)
        pyautogui.hotkey('win', 'up')
    elif position == "bottom_left":
        pyautogui.hotkey('win', 'left')
        time.sleep(0.4)
        pyautogui.hotkey('win', 'down')
    elif position == "bottom_right":
        pyautogui.hotkey('win', 'right')
        time.sleep(0.4)
        pyautogui.hotkey('win', 'down')
    time.sleep(1)  # Wait for the window to be positioned

def open_browsers():
    f=open("pythoncodes/webLibrary.txt")
 
    positions = ["top_left", "top_right", "bottom_left", "bottom_right"]

    for  position in positions:
        open_browser(f.readline())
        move_window_quarter(position)

if __name__ == "__main__":
    open_browsers()
# Wait for the window to be positioned




