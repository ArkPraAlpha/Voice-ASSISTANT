import os
import subprocess
import webbrowser
import shutil
def open_gmail_in_chrome():
# Try to find Chrome path
    chrome_path = None
    if os.name == 'nt':  # Windows
        chrome_path = shutil.which("chrome") or shutil.which("google-chrome")
        if not chrome_path:
            chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

    if os.path.exists(chrome_path):
        subprocess.Popen([chrome_path, "https://mail.google.com"])
        print("✅ Gmail opened in Google Chrome.")
    else:
        print("⚠️ Chrome not found. Opening Gmail in the default browser.")
        webbrowser.open("https://mail.google.com")


if __name__ == "__main__":
    open_gmail_in_chrome()