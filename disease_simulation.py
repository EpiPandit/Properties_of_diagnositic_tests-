import streamlit as st
import random

# Function to simulate sampling based on the chosen scenario's parameters
def sample_individual(prevalence, sensitivity, specificity):
    is_infected = random.random() < prevalence
    if is_infected:
        # True Positive or False Negative
        return "True Positive" if random.random() < sensitivity else "False Negative"
    else:
        # True Negative or False Positive
        return "True Negative" if random.random() < specificity else "False Positive"

# App title
st.title("Infectious Disease Diagnostic Simulation")

# Instructions for students
st.header("Instructions for Students")
st.write("""
You can perform multiple sampling events to gather your data. Based on the results you collect, calculate:
1. **Sensitivity**: The proportion of true positives among those who are actually infected.
2. **Specificity**: The proportion of true negatives among those who are not infected.
3. **Apparent Prevalence**: The proportion of positive test results in the population.
4. **Positive Predictive Value (PPV)**: The proportion of individuals with a positive test result who are actually infected.
5. **Negative Predictive Value (NPV)**: The proportion of individuals with a negative test result who are actually not infected.
""")

# Scenario details
scenarios = {
    "Scenario 1": {"prevalence": 0.10, "sensitivity": 0.90, "specificity": 0.95},
    "Scenario 2": {"prevalence": 0.90, "sensitivity": 0.90, "specificity": 0.95},
    "Scenario 3": {"prevalence": 0.90, "sensitivity": 0.80, "specificity": 0.68},
    "Scenario 4": {"prevalence": 0.20, "sensitivity": 0.85, "specificity": 0.85},
}

# Scenario selection
selected_scenario = st.selectbox("Select a scenario", list(scenarios.keys()))

# Initialize state to keep track of the sampling result
if 'result' not in st.session_state:
    st.session_state.result = None

# Sampling section
st.header("Sampling and Testing an Individual/Animal")

# Sample an individual when the button is clicked
if st.button("Sample an Individual"):
    st.session_state.result = sample_individual(
        scenarios[selected_scenario]["prevalence"],
        scenarios[selected_scenario]["sensitivity"],
        scenarios[selected_scenario]["specificity"],
    )
    st.write(f"Result: **{st.session_state.result}**")

# Clear the result when the Clear Results button is clicked
if st.session_state.result is not None:
    if st.button("Clear Results"):
        st.session_state.result = None
        st.write("Results cleared. You can sample again.")
