import streamlit as st
import joblib

model = joblib.load("model.pkl")
cv = joblib.load("vectorizer.pkl")

st.set_page_config(
    page_title="Email Spam Classifier",
    page_icon="📧",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

        body {
            font-family: 'Inter', sans-serif;
            background: #ffffff;
            color: #333;
        }

        .main-container {
            max-width: 700px;
            margin: 0 auto;
            padding: 20px;
        }

        .header {
            text-align: center;
            background: rgba(255, 255, 255, 0.95);
            padding: 30px;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
            margin-bottom: 30px;
        }

        .header h1 {
            font-size: 36px;
            font-weight: 700;
            color: #2c3e50;
            margin: 0;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
        }

        .header p {
            font-size: 16px;
            color: #7f8c8d;
            margin: 10px 0 0 0;
        }

        .input-section {
            background: rgba(255, 255, 255, 0.95);
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }

        .input-section h3 {
            font-size: 20px;
            font-weight: 600;
            color: #34495e;
            margin-bottom: 15px;
        }

        textarea {
            border: 2px solid #e1e8ed;
            border-radius: 10px;
            padding: 15px;
            font-size: 16px;
            font-family: 'Inter', sans-serif;
            resize: vertical;
            transition: border-color 0.3s ease;
        }

        textarea:focus {
            outline: none;
            border-color: #3498db;
            box-shadow: 0 0 0 3px rgba(52, 152, 219, 0.1);
        }

        .stButton>button {
            background: linear-gradient(135deg, #3498db, #2980b9);
            color: white;
            padding: 12px 30px;
            border-radius: 25px;
            border: none;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(52, 152, 219, 0.3);
        }

        .stButton>button:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(52, 152, 219, 0.4);
        }

        .result-section {
            background: rgba(255, 255, 255, 0.95);
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
            text-align: center;
        }

        .result-section h3 {
            font-size: 24px;
            font-weight: 600;
            margin-bottom: 15px;
        }

        .spam-result {
            color: #e74c3c;
            font-weight: 700;
        }

        .safe-result {
            color: #27ae60;
            font-weight: 700;
        }

        .footer {
            text-align: center;
            margin-top: 30px;
            font-size: 14px;
            color: #6c757d;
        }

        .footer a {
            color: #007bff;
            text-decoration: none;
        }

        .footer a:hover {
            text-decoration: underline;
        }

        .trust-badges {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-top: 20px;
        }

        .badge {
            background: rgba(255, 255, 255, 0.9);
            padding: 10px 15px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 500;
            color: #2c3e50;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-container'>", unsafe_allow_html=True)

st.markdown("""
    <div class='header'>
        <h1>📧 Email Spam Classifier</h1>
        <p>Advanced AI-powered spam detection to keep your inbox safe and secure.</p>
        <div class='trust-badges'>
            <div class='badge'>🔒 Secure & Private</div>
            <div class='badge'>⚡ Fast Analysis</div>
            <div class='badge'>🎯 High Accuracy</div>
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown("<div class='input-section'>", unsafe_allow_html=True)
st.markdown("<h3>Enter Your Email Content</h3>", unsafe_allow_html=True)
email = st.text_area(
    "Paste the email text here:",
    height=200,
    placeholder="Type or paste the email content you want to check for spam...",
    label_visibility="collapsed"
)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    predict_button = st.button("🔍 Analyze Email", use_container_width=True)

st.markdown("</div>", unsafe_allow_html=True)

if predict_button:
    if email.strip() == "":
        st.warning("⚠️ Please enter some email text to analyze.")
    else:
        with st.spinner("Analyzing your email..."):
            vector = cv.transform([email])
            result = model.predict(vector)[0]

        st.markdown("<div class='result-section'>", unsafe_allow_html=True)
        if result == 1:
            st.markdown("<h3 class='spam-result'>🚨 This email is SPAM!</h3>", unsafe_allow_html=True)
            st.markdown(
                "<p>Our AI has detected characteristics commonly found in spam emails. Exercise caution when interacting with this message.</p>",
                unsafe_allow_html=True)
        else:
            st.markdown("<h3 class='safe-result'>✅ This email appears SAFE</h3>", unsafe_allow_html=True)
            st.markdown("<p>No spam indicators detected. This email seems legitimate, but always stay vigilant.</p>",
                        unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

st.markdown("""
    <div class='footer'>
        <p>Built with ❤️ using Streamlit and Machine Learning</p>
        <p>For more information, visit our <a href="#">Privacy Policy</a> | <a href="#">Terms of Service</a></p>
    </div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
