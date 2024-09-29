import streamlit as st
from firebase_admin import credentials, auth
import home
cred = credentials.Certificate('streamlit-project-finalyear-afa5645a452c.json')

import mysql.connector
import bcrypt
import streamlit as st
import mysql.connector
import bcrypt  # For password hashing


# MySQL connection setup
def get_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="secret",
        database="disease_login"
    )
    return conn


# Function to create a user table if it doesn't exist
def create_user_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255) UNIQUE,
            email VARCHAR(255),
            password VARCHAR(255)
        )
    ''')
    conn.commit()
    cursor.close()
    conn.close()


# Function to add a user to the MySQL database
def add_user(username, email, password):
    conn = get_connection()
    cursor = conn.cursor()
    # Hash the password before storing
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    try:
        cursor.execute('INSERT INTO users (username, email, password) VALUES (%s, %s, %s)',
                       (username, email, hashed_password))
        conn.commit()
    except mysql.connector.Error as err:
        st.error(f"Error: {err}")
    finally:
        cursor.close()
        conn.close()


# Function to verify user during login
def verify_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT password FROM users WHERE username = %s', (username,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()

    if result:
        stored_password = result[0]
        # Verify password
        return bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8'))
    return False


# Function to handle redirection to another Streamlit app
def redirect_to_other_app():
    st.page_link('https://diseasepredictions.onrender.com',label="Redirect to Application")


# Main application logic
def app():
    # Create the user table if it doesn't exist
    create_user_table()

    # Display the title with custom CSS
    st.markdown('<h1 class="custom-title">Multi Disease Prediction Application</h1>', unsafe_allow_html=True)

    # Choose between Login and Sign Up
    choice = st.selectbox('Login / Sign Up', ['Login', 'Sign Up'])

    if choice == 'Login':
        username = st.text_input('Username:', placeholder='Enter the Username', key="username")
        password = st.text_input('Password:', placeholder='Enter the Password', type="password", key="password")

        if st.button('Login'):
            # Verify user credentials
            if verify_user(username, password):
                st.success('Login successful!')
                # Redirect to another app or page after login
                redirect_to_other_app()
            else:
                st.error('Invalid username or password')

    else:  # Sign Up
        username = st.text_input('Username', placeholder="Enter your Username", key="signup_username")
        email = st.text_input('Email', placeholder="Enter your Email", key="signup_email")
        password = st.text_input('Password', placeholder="Enter your Password", type="password", key="signup_password")

        if st.button('Create my Account'):
            try:
                add_user(username, email, password)
                st.success('Account Created Successfully')
                st.markdown('Please Login using your Username and Password')
                st.balloons()
            except Exception as e:
                st.error(f"Error: {e}")


app()
