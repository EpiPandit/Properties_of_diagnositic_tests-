import streamlit as st
import random

# Function to simulate sampling based on the chosen scenario's parameters
def sample_individual(prevalence, sensitivity, specificity):
    is_infected = random.random() < prevalence
    if is_infected:
        # True Positive or False Negative
        if random.random() < sensitivity:
            return "True Positive"
        else:
            return "False Negative"
    else:
        # True Negative or False Positive
        if random.random() < specificity:
            return "True Negative"
        else:
            return "False Positive"

# App title
st.title("Infectious Disease Diagnostic Simulation")

# Additional information for students
st.header("Instructions for Students")
st.write("""
You can perform multiple sampling events to gather your data. Based on the results you collect calculate:
- 1. **Sensitivity**: The proportion of true positives among those who are actually infected.
- 2. **Specificity**: The proportion of true negatives among those who are not infected.
- 3. **Apparent Prevalence**: The proportion of positive test results in the population.
- 4. **Positive Predictive Value (PPV)**: The proportion of individuals with a positive test result who are actually infected.
- 5. **Negative Predictive Value (NPV)**: The proportion of individuals with a negative test result who are actually not infected.
""")

# Scenario details
scenarios = {
    "Scenario 1": {"prevalence": 0.10, "sensitivity": 0.90, "specificity": 0.95},
    "Scenario 2": {"prevalence": 0.90, "sensitivity": 0.90, "specificity": 0.95},
    "Scenario 3": {"prevalence": 0.90, "sensitivity": 0.80, "specificity": 0.68},
    "Scenario 4": {"prevalence": 0.20, "sensitivity": 0.85, "specificity": 0.85},
}

# Scenario selection screen
st.header("Choose a disease scenario")
st.write("Click sample an individual and record the status of sampled individual")
st.write("To repeat click clear results and sample again")

# Dropdown menu for scenario selection
selected_scenario = st.selectbox("Select a scenario", list(scenarios.keys()))

# Show sampling options if a scenario is selected
if selected_scenario:
    st.header(f"Sampling an Individual - {selected_scenario}")

    # State to keep track of the result
    if 'result' not in st.session_state:
        st.session_state.result = None

    # Sample button
    if st.button("Sample an Individual"):
        st.session_state.result = sample_individual(
            scenarios[selected_scenario]["prevalence"],
            scenarios[selected_scenario]["sensitivity"],
            scenarios[selected_scenario]["specificity"],
        )

    # Display the result if it exists
    if st.session_state.result is not None:
        st.write(f"Result: **{st.session_state.result}**")

    # Clear results button
    if st.session_state.batch_results is not None:
        if st.button("Clear Results"):
            st.session_state.result = None
            st.write("Results cleared. You can sample again.")  
    # Display the clear result button only if there's a result
    #if st.button("Clear Result"):
        # Clear the result from session state
    #    st.session_state.result = None
    #    st.write("Results cleared. You can sample again.")
        # Refresh the UI by clearing the existing elements
        #st.experimental_set_query_params()

