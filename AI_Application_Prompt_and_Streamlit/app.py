# Imports 
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st

# laod API
from dotenv import load_dotenv
load_dotenv()

# Model initialized
model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
)

st.title("AI Fitness & Diet Coach")

age = st.number_input("Enter your Age", min_value=10, max_value=100)
gender = st.selectbox("Select your Gender", ["Male", "Female", "Other"])
height = st.number_input("Enter your Height (in feet)", min_value=2.0, max_value=8.0, step= 0.1)
weight = st.number_input("Enter your Weight (in kg)", min_value=10.0, max_value=200.0, step= 0.1)
goal = st.selectbox("Select your Goal", ["Weight Loss", "Weight Gain", "Muscle Gain", "Maintain"])
food_preferences = st.selectbox("Enter your Food Preferences", ["Vegetarian", "Non-Vegetarian", "Vegan"])
plan = st.number_input("Enter number of days for the plan", min_value=1, max_value=30)

prompt = f"""
You are a certified fitness and diet coach. 
You must follow the instructions carefully and stay within your expertise. 
If any information is missing or unclear, politely state the limitation instead of making up facts.
The user details are given below:
USER PROFILE:
Age: {age}
Gender: {gender}
Height: {height}
Weight: {weight}
Goal: {goal}
Food Preferences: {food_preferences}
Plan: {plan}
Based on this, provide:
1. BMI Analysis
2. Personalized Workout Plan
3. Personalized Diet Plan
IMPORTANT RULES:
- Do not provide medical advice, prescriptions, or supplements.
- If the request is unrelated to health/fitness, respond: "This app only supports fitness and diet plans."
- Keep the answer clear, step-by-step, and concise.
- Do not hallucinate or make up scientific terms or unsafe advice.
"""

if st.button("Generate Plan"): # terminal 
    with st.spinner("Generating Plan..."):
        result = model.invoke(prompt)
        st.subheader("Full Response")
        st.write(result.content) # print