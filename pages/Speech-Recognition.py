import streamlit as st
import speech_recognition as sr

def transcribe_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Please speak now...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        st.success("Transcription: {}".format(text))
    except Exception as e:
        st.error("Error: {}".format(e))

def main():
    st.title("Speech Recognition App")
    st.write("This app recognizes speech and transcribes it into text.")
    st.write("Click on the 'Start Transcription' button and start speaking.")

    if st.button("Start Transcription"):
        transcribe_speech()

if __name__ == "__main__":
    main()
