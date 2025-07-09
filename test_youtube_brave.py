#to open youtube in Brave browser(Microsoft store version)
import os
import time
def open_youtube_brave():
  
    try:
        print("Attempting to search for 'Python programming' on YouTube...")
        os.system("start brave https://www.youtube.com/results?search_query=Python+programming")
        print("Command sent to search for 'Python programming' on YouTube.")
    except Exception as e:
        print(f"Failed to search on YouTube: {e}")

def main():
    print("Starting YouTube Brave launcher...")
    time.sleep(2)  # Simulate some delay before opening
    open_youtube_brave()
    print("YouTube should now be open in Brave browser.")
if __name__ == "__main__":
    main()
