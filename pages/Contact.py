import requests
import streamlit as st
from streamlit_lottie import st_lottie




def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding=load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_8kut1rsr.json")

 # ---- CONTACT ----
st.write("---")
st.header("Get In Touch With Me!")
st.write("##")

# Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
# contact_form = """
# <form action="https://formsubmit.co/kouissar@gmail.com" method="POST">
#     <input type="hidden" name="_captcha" value="false">
#     <input type="text" name="name" placeholder="Your name" required>
#     <input type="email" name="email" placeholder="Your email" required>
#     <textarea name="message" placeholder="Your message here" required></textarea>
#     <button type="submit">Send</button>
# </form>
# """


left_column, right_column = st.columns(2)
with right_column:
    # st.markdown(contact_form, unsafe_allow_html=True)
    st.write('nothing')
with left_column:
    # st.empty()
    st_lottie(
        lottie_coding,
        speed=1,
        reverse=False,
        loop=True,
        quality="low", #medium, high
        # renderer="svg", #canvas
        height="None",
        width="None",
        key="None",)
    




# Define the FormSubmit.co API endpoint
API_ENDPOINT = "https://formsubmit.co/kouissar@gmail.com"

# Define the app layout
# st.set_page_config(page_title="Contact Form", page_icon=":email:")
st.markdown("# Contact Us")
st.markdown("Please fill out the form below to get in touch with us.")
st.markdown("")

# Define the form fields
name = st.text_input("Name")
email = st.text_input("Email")
message = st.text_area("Message")

# Define the form submission function
def submit_form():
    # Define the form data
    data = {
        "name": name,
        "email": email,
        "message": message
    }
    # Send the form data to FormSubmit.co
    response = requests.post(API_ENDPOINT, data=data)
    # Show the submission status
    if response.status_code == 200:
        st.success("Your message has been sent!")
    else:
        st.error("Oops! Something went wrong. Please try again later.")

# Add a submit button to the form
if st.button("Submit"):
    submit_form()
