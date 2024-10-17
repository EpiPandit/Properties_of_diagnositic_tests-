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
import streamlit as st

st.markdown("""
## Infectious Disease Diagnostic Simulation Guide

### Setup
1. Form groups and position yourselves near your sister groups.
2. Locate the grid on the board for reporting group results.

### Instructions
1. **Individual Sampling**: Each group member should sample 5 times using the "Sample an Individual" button.
2. **Group Analysis**: 
   - Compile your group's results into a 2x2 table.
   - Calculate:
     - Sensitivity
     - Specificity
     - Positive Predictive Value (PPV)
     - Negative Predictive Value (NPV)
     - True Prevalence
     - Apparent Prevalence
3. **Reporting**: One group member should report your table and calculated values on the board.

### Scenarios
You will work through multiple scenarios:

#### Scenario 1
- Complete the exercise within your initial group.
- After all groups report, note the overall class prevalence, sensitivity, and specificity.

#### Scenario 2
- Combine with your sister group to form a larger group.
- Repeat the analysis with the combined data.
- When called upon, report:
  - Comparison of your combined group's true prevalence to the overall class prevalence.
  - Your thoughts on how representative your sample is of the entire class.
  - Any insights on the potential condition/outcome being simulated.

#### Scenario 3
- This scenario will involve a different class-wide approach.
- Follow the instructor's guidance for compiling and analyzing data as a full class.

### Reflection
- Consider the effectiveness of the simulated diagnostic test.
- Discuss its potential utility if it were the only available option.
- Participate in the concluding review to help improve future iterations of this exercise.
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
