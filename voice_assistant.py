# Requires: pip install pyttsx3
import pyttsx3
import datetime
import webbrowser

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)  # Print for reference
    engine.say(text)
    engine.runAndWait()

def main():
    speak("Hello! I am your assistant. How can I help you today?")

    while True:
        command = input("You: ").lower()

        if "time" in command:
            time_now = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {time_now}")

        elif "date" in command:
            today = datetime.date.today().strftime("%B %d, %Y")
            speak(f"Today's date is {today}")

        elif "open youtube" in command:
            webbrowser.open("https://youtube.com")
            speak("Opening YouTube")

        elif "open google" in command:
            webbrowser.open("https://google.com")
            speak("Opening Google")

        elif "open instagram" in command:
            webbrowser.open("https://instagram.com")
            speak("Opening Instagram")

        elif "stop" in command or "exit" in command:
            speak("Goodbye! Have a great day.")
            break

        else:
            speak("Sorry, I can only tell time, date, or open YouTube, Google, and Instagram for now.")

if _name_ == "_main_":
    main()
