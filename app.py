import streamlit as st
import pandas as pd
import datetime
from datetime import date
import os.path, time
import numpy as np
import plotly.express as px
import plotly.graph_objs as go
from IPython.display import HTML



st.set_page_config(
    page_title="My Digital Zen World", layout="wide", initial_sidebar_state='expanded'
)

# # Use local CSS
# def local_css(file_name):
#     with open(file_name) as f:
#         st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Define the YouTube video ID
YOUTUBE_VIDEO_ID = "tybOi4hjZFQ"

# Define the HTML code to embed the video
HTML_CODE = f"""
<div align="center">
  <iframe width="560" height="315" src="https://www.youtube.com/embed/{YOUTUBE_VIDEO_ID}" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen>
  </iframe>
</div>
"""

# Define a list of rules based on the Tao Te Ching
rules = [
    "Simplicity, patience, compassion.",
    "Be content with what you have; rejoice in the way things are. When you realize there is nothing lacking, the whole world belongs to you.",
    "Nature does not hurry, yet everything is accomplished.",
    "The wise man does not lay up his own treasures. The more he gives to others, the more he has for his own.",
    "He who knows, does not speak. He who speaks, does not know.",
    "To the mind that is still, the whole universe surrenders.",
]
fasting = [
        "Intermittent fasting (IF) has been shown to have several health benefits. It involves restricting food intake for certain periods of time, typically between 12 to 24 hours. One of the main benefits of IF is weight loss, as it can help reduce calorie intake and increase metabolism",
        "One popular method is the 16/8 method, where you fast for 16 hours and eat within an 8-hour window each day. For example, you might eat from 12 pm to 8 pm and then fast until noon the next day."]

tao_te_ching_quotes = [ "The journey of a thousand miles begins with one step. - Chapter 64",    
        "Knowing others is intelligence; knowing yourself is true wisdom. Mastering others is strength; mastering yourself is true power. - Chapter 33",    
        "Nature does not hurry, yet everything is accomplished. - Chapter 43",    
        "The wise man is one who, knows, what he does not know. - Chapter 71",    
        "He who knows that enough is enough will always have enough. - Chapter 46",    
        "When you are content to be simply yourself and don't compare or compete, everyone will respect you. - Chapter 8",    
        "In dwelling, live close to the ground. In thinking, keep to the simple. In conflict, be fair and generous. In governing, don't try to control. In work, do what you enjoy. In family life, be completely present. - Chapter 8",    
        "When I let go of what I am, I become what I might be. - Chapter 44",    
        "The softest things in the world overcome the hardest things in the world. - Chapter 43",    
        "The more that laws and regulations are given prominence, the more thieves and robbers there will be. - Chapter 57"]




# local_css("style/style.css")
data_file = 'data/data.csv'
def get_data_from_csv(path):
    df = pd.read_csv(path, header=0, sep=',')
    return df

df = get_data_from_csv(data_file)
now = datetime.datetime.now()
today = now.strftime("%Y-%m-%d %H:%M:%S")
df['Date'] = pd.to_datetime(df['Date'])
total_rec=df.shape[0]
total_duration=df['Duration'].sum()
by_month=pd.to_datetime(df['Date']).dt.to_period('M').value_counts().sort_index()
by_week=pd.to_datetime(df['Date']).dt.to_period('W').value_counts().sort_index()
by_day=pd.to_datetime(df['Date']).dt.to_period('D').value_counts().sort_index()
df_day=by_day.rename_axis('day').reset_index(name='counts')
df_week=by_week.rename_axis('week').reset_index(name='counts')
count_by_activity=df.groupby(['Activity'])['Activity'].count()



fig_daily_trend= go.Figure(data=go.Bar(x=df_day['day'].astype(dtype=str), y=df_day['counts'], marker_color='indianred'))
fig_weekly_trend= go.Figure(data=go.Bar(x=df_week['week'].astype(dtype=str), y=df_week['counts'], marker_color='indianred'))
fig_act_dist=px.pie(count_by_activity, values='Activity', names=count_by_activity.index, hole=0.5, title='Activity Distribution')


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
    st.markdown('<h4>Activity Added Successfully!</h4>', unsafe_allow_html=True)
    df = df.append(d, ignore_index = True)
    df.to_csv(data_file, index=False, header=True)
st.sidebar.checkbox("Use Container width", value=False, key="use_container_width")

# Header Section 
with st.container():
    st.subheader("Hi, I am Rafik :wave:")
    st.title("And I am From Maryland, USA")
    st.write("I've been doing a lots of research recently on how to live well and to optimize key aspects of my life. I would like to share with you my findings via this project. I hope you find this project insightful and inspiring! Let me know if you have any other questions.")
    #sp.speak("Hi, I am Rafik. A Software Engineer From USA.I am passionate about coding, fishing, and music. What about you? ")



tab1, tab2, tab3, tab4, tab5 = st.tabs(["Data", "Analysis", "Tao Te Ching Rules", "Intermittent fasting (IF)", "Wim Hof Method"])
with tab1:
    st.dataframe(df, use_container_width=st.session_state.use_container_width)
with tab2:
    col1, col2, col3 = st.columns(3)
    col1.plotly_chart(fig_daily_trend, theme="streamlit", use_container_width=True)
    col2.plotly_chart(fig_weekly_trend, theme="streamlit", use_container_width=True)
    col3.plotly_chart(fig_act_dist, theme="streamlit", use_container_width=True)
with tab3:
    # Display each rule in a numbered list
    for i, rule in enumerate(tao_te_ching_quotes):
        st.write(f"{i+1}. {rule}")
    
with tab4: 
       # Display each rule in a numbered list
    for i, rule in enumerate(fasting):
        st.write(f"{i+1}. {rule}")
with tab5:
    # Embed the YouTube video
    st.markdown(HTML_CODE, unsafe_allow_html=True)
