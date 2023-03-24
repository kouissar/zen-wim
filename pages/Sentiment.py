import streamlit as st
from textblob import TextBlob

st.title("Sentiment Analysis App")

# Get user input
text = st.text_input("Enter some text:")

# Perform sentiment analysis
if text:
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity

    # Determine sentiment label
    if sentiment > 0:
        label = "Positive"
    elif sentiment < 0:
        label = "Negative"
    else:
        label = "Neutral"

    # Display result
    st.write("Sentiment:", label)
