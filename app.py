import streamlit as st
import pandas as pd
import datetime
from datetime import date



st.set_page_config(
    page_title="My Digital Zen World", layout="wide"
)

# # Use local CSS
# def local_css(file_name):
#     with open(file_name) as f:
#         st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# local_css("style/style.css")
data_file = 'data/data.csv'
def get_data_from_csv(path):
    df = pd.read_csv(path, header=0, sep=',')
    return df

df = get_data_from_csv(data_file)
now = datetime.datetime.now()
today = now.strftime("%Y-%m-%d %H:%M:%S")
#sidebar
st.sidebar.subheader("Enter a new activity")
activity = st.sidebar.selectbox('Select the activity', options=['Wim Hof Breathing', '4-7-8 Breathing', 'Cold Shower', '10 mins Meditation', 'Walk'])
duration = st.sidebar.text_input('Enter a duration', 0)

click_submit = st.sidebar.button("Submit")
st.title(':palm_tree: Mindfullness Tracker')
if click_submit == True:
    d = {'Date': today,
         'Activity': activity,
         'Duration': duration
         }
    st.markdown('<h3>Thank you for your feedback!</h3>', unsafe_allow_html=True)
    df = df.append(d, ignore_index = True)
    df.to_csv(data_file, index=False, header=True)

st.dataframe(df)
