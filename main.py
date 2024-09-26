import speech_recognition as sr
import pyttsx3
import webbrowser
import pyautogui
import pyperclip
import time
import web

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()


def process_command(command):
    command = command.lower()
    print(command)
    
    if command == "open google":
        webbrowser.open("https://www.google.co.in/")
    elif command == "open youtube":
        webbrowser.open("https://www.youtube.co.in/")
    elif command == "open asc":
        webbrowser.open("https://asc.iitb.ac.in/acadmenu/index.jsp")
    elif "portal" in command:
        webbrowser.open("https://portal.iitb.ac.in/asc/Login")
    elif command == "open whatsapp":
        webbrowser.open("https://web.whatsapp.com/")
    elif "minimise" in command:
        pyautogui.hotkey('win','d')
    elif command=="open workspace":
        web.main()
    elif "open" in command:
        website=command.split(" ")[1]
        webbrowser.open(f"https://www.{website}.com")
    elif command.startswith("play"):
        song = command.replace("play","").strip()
        pyperclip.copy(song)
        webbrowser.open("https://www.youtube.co.in/")
        time.sleep(6)
        pyautogui.moveTo(975, 224)
        pyautogui.click()
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.moveTo(560, 572)
        pyautogui.click()

        
def listen_for_command():
    try:
        with sr.Microphone() as source:
            print("Listening for command...")
            # recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source, timeout=2, phrase_time_limit=1.5)
            print("Recognizing...")
            return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
    except sr.WaitTimeoutError:
        pass
    return None

def main():
    speak("Initializing Jarvis....")
    while True:
        word = listen_for_command()
        # classified_word = classify_command(word)
        if word and "jarvis" in word.lower():
            word1 = word.lower().replace("jarvis", "").strip()
            if word1 == "":
                speak("hello")
            else:
                speak(word1)
            command = listen_for_command()
            if command:
                # classified_command = command(command)
                process_command(command)

if __name__ == "__main__":
    main()
