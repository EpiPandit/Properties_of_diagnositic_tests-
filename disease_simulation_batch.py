import streamlit as st
import random

# Function to simulate sampling of 100 individuals based on the chosen scenario's parameters
def sample_individuals(prevalence, sensitivity, specificity, num_samples=100):
    results = {"True Positive": 0, "False Positive": 0, "True Negative": 0, "False Negative": 0}
    
    for _ in range(num_samples):
        is_infected = random.random() < prevalence
        if is_infected:
            # True Positive or False Negative
            if random.random() < sensitivity:
                results["True Positive"] += 1
            else:
                results["False Negative"] += 1
        else:
            # True Negative or False Positive
            if random.random() < specificity:
                results["True Negative"] += 1
            else:
                results["False Positive"] += 1
    
    return results

# App title
st.title("Infectious Disease Diagnostic Simulation - Batch Sampling")
st.write("""
You can perform multiple sampling events to gather your data. Based on the results you collect calculate:
1. **Sensitivity**: The proportion of true positives among those who are actually infected.
2. **Specificity**: The proportion of true negatives among those who are not infected.
3. **Apparent Prevalence**: The proportion of positive test results in the population.
4. **Positive Predictive Value (PPV)**: The proportion of individuals with a positive test result who are actually infected.
5. **Negative Predictive Value (NPV)**: The proportion of individuals with a negative test result who are actually not infected.
""")
# Scenario selection screen
st.header("Choose a Scenario")

# Scenario details
scenarios = {
    "Scenario 1": {"prevalence": 0.10, "sensitivity": 0.90, "specificity": 0.95},
    "Scenario 2": {"prevalence": 0.90, "sensitivity": 0.90, "specificity": 0.95},
    "Scenario 3": {"prevalence": 0.90, "sensitivity": 0.80, "specificity": 0.68},
    "Scenario 4": {"prevalence": 0.20, "sensitivity": 0.85, "specificity": 0.85},
}

# Display scenario options
selected_scenario = st.selectbox("Select a scenario", list(scenarios.keys()))

# Show scenario details
#st.write(f"**Prevalence**: {scenarios[selected_scenario]['prevalence'] * 100}%")
#st.write(f"**Sensitivity**: {scenarios[selected_scenario]['sensitivity'] * 100}%")
#st.write(f"**Specificity**: {scenarios[selected_scenario]['specificity'] * 100}%")

# State to keep track of the results
if 'batch_results' not in st.session_state:
    st.session_state.batch_results = None

# Sampling screen
st.header("Batch Sampling and Testing of 100 Individuals/Animals")

# Sample button
if st.button("Sample and Test 100 Individuals/Animals"):
    st.session_state.batch_results = sample_individuals(
        scenarios[selected_scenario]["prevalence"],
        scenarios[selected_scenario]["sensitivity"],
        scenarios[selected_scenario]["specificity"],
        num_samples=100
    )
    # Display results for each category
    st.subheader("Batch Sampling Results")
    st.write(f"True Positives: {st.session_state.batch_results['True Positive']}")
    st.write(f"False Positives: {st.session_state.batch_results['False Positive']}")
    st.write(f"True Negatives: {st.session_state.batch_results['True Negative']}")
    st.write(f"False Negatives: {st.session_state.batch_results['False Negative']}")

# Clear results button
if st.session_state.batch_results is not None:
    if st.button("Clear Results"):
        st.session_state.batch_results = None
        st.write("Results cleared. You can sample again.")


