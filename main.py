import streamlit as st
from firebase_admin import credentials, auth
cred = credentials.Certificate('streamlit-project-finalyear-afa5645a452c.json')


# Function to load custom CSS styles
def load_css():
    st.markdown(
        """
        <style>
        /* Custom CSS for title font with hover animation */
        .custom-title {
            font-size: 32px;
            color: #fff;  /* Base font color */
            text-align: center;
            font-family: Verdana, Geneva, Tahoma, sans-serif;
            font-weight: bold;
            transition: color 0.3s ease-in-out;
        }
        .custom-title:hover {
            color: #ff6666; /* Change to your preferred color on hover */
        }

        /* Custom CSS for form text */
        .custom-text {
            font-size: 18px;
            color: #555555;
            transition: font-size 0.3s ease-in-out;
        }

        /* Button styling */
        button {
            background-color: #4CAF50;
            color: white;
            padding: 12px 18px;
            margin: 8px 0;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            width: 70%;  /* Make button size match the input fields */
            font-size: 14px;  /* Adjust button font size */
            transition: background-color 0.3s ease;
        }
        button:hover {
            background-color: #45a049;
        }

        /* Responsive design for smaller screens */
        @media (max-width: 768px) {
            .custom-title {
                font-size: 24px;
            }
        }

        </style>
        """,
        unsafe_allow_html=True
    )


# Function to handle redirection to another Streamlit app
def redirect_to_other_app():
    # Simulating redirection by changing app state
    # Replace 'other_streamlit_app' with your actual page logic or Streamlit app URL
    st.rerun()


# Main application logic
def app():
    # Load custom CSS
    load_css()

    # Display the title with custom CSS and hover effect
    st.markdown('<h1 class="custom-title">Multi Disease Prediction Application</h1>', unsafe_allow_html=True)

    # Choose between Login and Sign Up
    choice = st.selectbox('Login / Sign Up', ['Login', 'Sign Up'])

    # Form elements with custom styling
    if choice == 'Login':
        username = st.text_input('Username:', placeholder='Enter the Username', key="username")
        password = st.text_input('Password:', placeholder='Enter the Password', type="password", key="password")

        if st.button('Login'):
            # Simulate login logic
            # Ideally, you'd validate the username and password with Firebase or another service
            # For now, simulate successful login
            st.success('Login successful!')
            # Redirect to another app or page after login
            redirect_to_other_app()
    else:
        username = st.text_input('Username', placeholder="Enter your Username", key="signup_username")
        email = st.text_input('Email', placeholder="Enter your Email", key="signup_email")
        password = st.text_input('Password', placeholder="Enter your Password", type="password", key="signup_password")

        if st.button('Create my Account'):
            # Simulate account creation
            st.success('Account Created Successfully')
            st.markdown('Please Login using your Username and Password')
            st.balloons()


app()
