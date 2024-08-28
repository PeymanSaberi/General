import subprocess
import time
import pyautogui

def main():
    # Auto input
    hostname = "IP Address Server"
    username = 'Insert username'
    password = 'Insert password'

    
    # مسیر به فایل اجرایی PuTTY
    putty_path = r"C:\Program Files\PuTTY\putty.exe"
    
    # اجرای PuTTY با نام کاربری و IP
    subprocess.Popen([putty_path, f"{username}@{hostname}"])
    time.sleep(10)

    pyautogui.typewrite("Insert password")
    pyautogui.hotkey("enter")
    time.sleep(5)

    pyautogui.typewrite("Number of menu for reset software")
    pyautogui.hotkey("enter")
    time.sleep(5)

    pyautogui.typewrite("Number of menu for reset software")
    pyautogui.hotkey("enter")
    time.sleep(5)

    pyautogui.typewrite("y")
    time.sleep(20)

    pyautogui.typewrite("Insert password")
    pyautogui.hotkey("enter")
    time.sleep(15)

    pyautogui.typewrite("0")
    pyautogui.hotkey("enter")
    time.sleep(5)
    
    return
    
    

if __name__ == "__main__":
    main()
