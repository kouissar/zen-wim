import streamlit as st
import pandas as pd

st.set_page_config(page_title="Login Page")

st.write("# Login")

# Load data (user credentials)
data_file="data/user_credentials.csv"
data = pd.read_csv(data_file)

# Allow user to select login or registration
option = st.radio("Choose an option", ["Login", "Register"])

# Login
if option == "Login":
    # Allow user to enter username and password
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # Validate user credentials
    if username and password:
        if data[(data["username"] == username) & (data["password"] == password)].empty:
            st.write(username, password)
            st.session_state.user = username
            st.write(f"Welcome, {username}!")
            st.write("Invalid username or password.")
        else:
            # Store user session
            st.session_state.user = username
            st.write(f"Welcome, {username}!")

# Registration
elif option == "Register":
    # Allow user to enter new username and password
    new_username = st.text_input("New Username")
    new_password = st.text_input("New Password", type="password")

    # Validate new user credentials
    if new_username and new_password:
        if not data[data["username"] == new_username].empty:
            st.write("Username already exists.")
        else:
            # Add new user credentials to data and save to file
            print("in data save")
            new_data = pd.DataFrame({"username": [new_username], "password": [new_password]})
            data = pd.concat([data, new_data], ignore_index=True)
            data.to_csv(data_file, index=False)
            st.write("Registration successful. Please log in.")
