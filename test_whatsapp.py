import os
import time

def open_whatsapp():
    try:
        print("Attempting to open WhatsApp...")
        os.system("start whatsapp:")
        print("Command sent to open WhatsApp.")
    except Exception as e:
        print(f"Failed to open WhatsApp: {e}")


def main():
    print("Starting WhatsApp launcher...")
    time.sleep(2)  # Simulate some delay before opening
    open_whatsapp()
    print("WhatsApp should now be open.")

if __name__ == "__main__":
    main()
    
