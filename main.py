import streamlit as st
import pickle

# Set the background color of the page to light blue
st.markdown("""
    <style>
    body {
        background-color: #e0f7fa;
    }
    .center-button {
        display: flex;
        justify-content: center;
    }
    </style>
    """, unsafe_allow_html=True)

# Using columns to place the image beside the heading
col1, col2 = st.columns([1, 3])

# Add image in the first column
with col1:
    st.image("D:\\proj4\\techsaksham\\54-512new.jpg", width=150)

# Add the title in the second column
with col2:
    st.title("Email Spam Classification Application")

st.write("Welcome to the ultimate email classifier! This intelligent machine learning app swiftly identifies and classifies your emails as spam or not")
st.subheader("Spam Detection Engine")

# Try loading the model and vectorizer
try:
    model = pickle.load(open('D:\\proj4\\techsaksham\\spam.pkl', 'rb'))
    cv = pickle.load(open('D:\\proj4\\techsaksham\\vec.pkl', 'rb'))
except Exception as e:
    st.error(f"Error loading files: {e}")
    st.stop()

def main():
    # Input text area for the user
    user_input = st.text_area("Enter an email to classify", height=150)

    # Add the button inside a centered div
    st.markdown('<div class="center-button">', unsafe_allow_html=True)
    classify_button = st.button("Classify")
    st.markdown('</div>', unsafe_allow_html=True)

    if classify_button:
        if user_input:
            try:
                # Prepare the data
                data = [user_input]
                vec = cv.transform(data).toarray()

                # Predict
                result = model.predict(vec)

                # Display result with styling
                if result[0] == 0:
                    st.success("This is not a spam email")
                else:
                    st.error("This is a spam email")
            except Exception as e:
                st.error(f"Error in prediction: {e}")
        else:
            st.write("Please enter an email to classify.")

# Run the app
if __name__ == '__main__':
    main()
