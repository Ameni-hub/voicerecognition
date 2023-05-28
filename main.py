import streamlit as st
import speech_recognition as sr

def greet_person(name):
    st.write(f"Hello, {name}!")

def calculate_sum(num1, num2):
    return num1 + num2

def transcribe_speech():
    # Initialize recognizer class
    r = sr.Recognizer()
    # Reading Microphone as source
    with sr.Microphone() as source:
        st.info("Speak now...")
        # listen for speech and store in audio_text variable
        audio_text = r.listen(source)
        st.info("Transcribing...")

        try:
            # using Google Speech Recognition
            text = r.recognize_google(audio_text)
            return text
        except:
            return "Sorry, I did not get that."

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    st.title("Speech Recognition App")
    st.write("Click on the buttons to perform actions:")

    if st.button("Talk Free"):
        transcribed_text = transcribe_speech()
        st.write("Transcription: ", transcribed_text)

    if st.button("Greet"):
        transcribed_name = transcribe_speech()
        greet_person(transcribed_name)

    if st.button("Number"):
        transcribed_num1 = transcribe_speech()
        transcribed_num2 = transcribe_speech()
        try:
            num1 = int(transcribed_num1)
            num2 = int(transcribed_num2)
            result = calculate_sum(num1, num2)
            st.write(f"Sum of {num1} and {num2}:", result)
        except ValueError:
            st.write("Please speak valid numbers.")
