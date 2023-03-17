import streamlit as st
import pandas as pd
import datetime
from datetime import date
import os.path, time
import numpy as np
import plotly.express as px
import plotly.graph_objs as go



st.set_page_config(
    page_title="My Digital Zen World", layout="wide", initial_sidebar_state='expanded'
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
    st.write("I am a highly motivated individual with a passion for coding, music, and outdoor adventures. In my free time, I enjoy hiking and camping in the great outdoors, as well as playing and composing music. I am always looking for new challenges and ways to learn and grow, both personally and professionally. Whether I'm coding a new software application or exploring the wilderness, I am driven by my love of problem-solving and creation.")
    #sp.speak("Hi, I am Rafik. A Software Engineer From USA.I am passionate about coding, fishing, and music. What about you? ")

tab1, tab2, tab3 = st.tabs(["Data", "Analysis", "Russian Mafia Boss Rules"])
with tab1:
    st.dataframe(df, use_container_width=st.session_state.use_container_width)
with tab2:
    col1, col2, col3 = st.columns(3)
    col1.plotly_chart(fig_daily_trend, theme="streamlit", use_container_width=True)
    col2.plotly_chart(fig_weekly_trend, theme="streamlit", use_container_width=True)
    col3.plotly_chart(fig_act_dist, theme="streamlit", use_container_width=True)


