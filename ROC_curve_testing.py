import streamlit as st
import random
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to generate a dog's T4 or T3 value and disease status
def generate_dog_data(test_type, breed):
    breed_prevalence = {
        "Golden Retriever": 0.60,
        "Shih-tzu": 0.05,
        "Alaskan Malamute": 0.35
    }
    is_hypothyroid = random.random() < breed_prevalence[breed]
    
    if test_type == 'T4':
        if is_hypothyroid:
            value = random.uniform(5, 20)  # Lower T4 values for hypothyroid dogs
        else:
            value = random.uniform(15, 50)  # Normal to high T4 values for healthy dogs
        
        # Add some noise to simulate imperfect data
        value += random.uniform(-5, 5)
        
        # Ensure T4 value is not negative
        value = max(0, value)
    else:  # T3
        if is_hypothyroid:
            value = random.uniform(10, 40)  # Lower T3 values for hypothyroid dogs
        else:
            value = random.uniform(30, 100)  # Normal to high T3 values for healthy dogs
        
        # Add more noise to T3 to simulate higher error rate
        value += random.uniform(-10, 10)
        
        # Ensure T3 value is not negative
        value = max(0, value)
    
    return round(value, 2), is_hypothyroid

# App title
st.title("Canine Hypothyroidism Diagnostic Simulation")

# Instructions for students
st.header("Instructions for Students")

st.markdown("""
## Canine Hypothyroidism Diagnostic Simulation: Student Guide
### Background
Hypothyroidism is a common endocrine disorder in dogs, characterized by insufficient production of thyroid hormones. Accurate diagnosis is crucial for proper treatment and management of the condition. Two key thyroid hormones used in diagnosing hypothyroidism are:

1. **Thyroxine (T4)**: The primary hormone produced by the thyroid gland.
2. **Triiodothyronine (T3)**: The active form of thyroid hormone, converted from T4.

### Diagnostic Challenges

Diagnosing hypothyroidism can be challenging due to several factors:

1. Overlap in hormone levels between healthy and hypothyroid dogs.
2. Variations in individual dogs' normal hormone ranges.
3. Influence of non-thyroidal factors on hormone levels.
4. Differences in test accuracy between T4 and T3 measurements.

### Simulation Exercise

This simulation allows you to explore the challenges of diagnosing hypothyroidism using either T4 or T3 tests. You'll sample a population of dogs, analyze their hormone levels, and set diagnostic thresholds to classify them as hypothyroid or healthy.

### Instructions

1. **Choose Your Test**: Select either T4 or T3 for testing. Note that T4 is generally considered more reliable for initial screening.

2. **Sample Size**: Decide how many dogs to sample (1-200). Larger samples provide more data but may take longer to analyze.

3. **Generate Data**: Click "Sample Dogs" to create your dataset.

4. **Analyze the Data**:
   - Examine the strip plot showing hormone levels for hypothyroid and normal dogs.
   - Note the overlap between the two groups and the position of the normal range lines.

5. **Set a Diagnostic Threshold**:
   - Use the slider to set a hormone level below which you'll classify dogs as hypothyroid.
   - Consider the trade-offs between sensitivity (correctly identifying hypothyroid dogs) and specificity (correctly identifying healthy dogs).

6. **Evaluate Your Threshold**:
   - Observe how sensitivity and specificity change as you adjust the threshold.
   - Examine the confusion matrix to understand the implications of false positives and false negatives.

7. **Compare T4 and T3**:
   - Repeat the process for both hormones.
   - Note any differences in the difficulty of setting an accurate threshold.

8. **Reflect on the Challenges**:
   - How does the overlap between hypothyroid and normal dogs affect diagnosis?
   - What are the implications of false positives vs. false negatives in a clinical setting?
   - Why might T4 be preferred over T3 for initial screening?

### Key Concepts to Consider

- **Sensitivity**: The ability of the test to correctly identify dogs with hypothyroidism.
- **Specificity**: The ability of the test to correctly identify dogs without hypothyroidism.
- **False Positives**: Healthy dogs incorrectly diagnosed as hypothyroid.
- **False Negatives**: Hypothyroid dogs incorrectly classified as healthy.
- **Prevalence**: The proportion of hypothyroid dogs in the population (set to 30% in this simulation).

### Normal Ranges (for reference)

- T4: 12-45 nmol/l
- T3: 20-90 ng/dl

Remember, these ranges are guidelines. In practice, individual variation and other factors can complicate diagnosis.

### Conclusion

This simulation demonstrates the complexities of diagnosing hypothyroidism in dogs. In real clinical settings, veterinarians often use multiple tests and consider the dog's overall health and symptoms when making a diagnosis. The exercise highlights the importance of understanding test limitations and the need for careful interpretation of diagnostic results.

### Additional Information on Breed-Specific Prevalence

In this simulation, we've included three breed-specific populations:

1. Golden Retrievers
2. Shih-tzu
3. Alaskan Malamutes

Consider how these different prevalence rates might affect your diagnostic approach and interpretation of results.
""")

# Breed selection
st.header("Select Dog Breed")
breed = st.radio("Choose a breed", ('Golden Retriever', 'Shih-tzu', 'Alaskan Malamute'))

# Test type selection
st.header("Which Thyroid Hormone would you like to test?")
test_type = st.radio("Select test type", ('T4', 'T3'))

# Number of dogs to sample
num_dogs = st.slider("Number of dogs to sample", 30, 200, 30)

# Initialize state to keep track of the sampled dogs
if 'dogs_data' not in st.session_state:
    st.session_state.dogs_data = None

# Sample dogs when the button is clicked
if st.button("Sample Dogs"):
    st.session_state.dogs_data = [generate_dog_data(test_type, breed) for _ in range(num_dogs)]

# Display data and plot if dogs have been sampled
if st.session_state.dogs_data is not None:
    # Create a DataFrame from the sampled data
    df = pd.DataFrame(st.session_state.dogs_data, columns=[f'{test_type} Value', 'Is Hypothyroid'])
    df['Status'] = df['Is Hypothyroid'].map({True: 'Hypothyroid', False: 'Normal'})
    
    # Display the data
    st.write(f"Sampled {breed} Data:")
    st.dataframe(df)
    
    # Create a strip plot
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.stripplot(x='Status', y=f'{test_type} Value', data=df, jitter=True, ax=ax)
    ax.set_ylabel(f'{test_type} Value ({("nmol/l" if test_type == "T4" else "ng/dl")})')
    ax.set_title(f'{test_type} Values of Sampled {breed}s')
    
    if test_type == 'T4':
        ax.axhline(y=12, color='green', linestyle='--', label='Lower Normal Limit')
        ax.axhline(y=45, color='green', linestyle='--', label='Upper Normal Limit')
    else:  # T3
        ax.axhline(y=20, color='green', linestyle='--', label='Lower Normal Limit')
        ax.axhline(y=90, color='green', linestyle='--', label='Upper Normal Limit')
    
    plt.legend()
    st.pyplot(fig)

    # Threshold selection and evaluation
    st.header("Threshold Selection and Evaluation")
    if test_type == 'T4':
        threshold = st.slider(f"Select {test_type} threshold for hypothyroidism diagnosis", 0.0, 50.0, 12.0, 0.1)
    else:  # T3
        threshold = st.slider(f"Select {test_type} threshold for hypothyroidism diagnosis", 0.0, 100.0, 20.0, 0.1)
    
    df['Diagnosed Hypothyroid'] = df[f'{test_type} Value'] < threshold
    
    true_positives = ((df['Is Hypothyroid'] == True) & (df['Diagnosed Hypothyroid'] == True)).sum()
    true_negatives = ((df['Is Hypothyroid'] == False) & (df['Diagnosed Hypothyroid'] == False)).sum()
    false_positives = ((df['Is Hypothyroid'] == False) & (df['Diagnosed Hypothyroid'] == True)).sum()
    false_negatives = ((df['Is Hypothyroid'] == True) & (df['Diagnosed Hypothyroid'] == False)).sum()
    
    sensitivity = true_positives / (true_positives + false_negatives) if (true_positives + false_negatives) > 0 else 0
    specificity = true_negatives / (true_negatives + false_positives) if (true_negatives + false_positives) > 0 else 0
    
    st.write(f"Sensitivity: {sensitivity:.2f}")
    st.write(f"Specificity: {specificity:.2f}")
    
    # Confusion matrix
    st.write("Confusion Matrix:")
    confusion_matrix = pd.DataFrame({
        'Actual Hypothyroid': [true_positives, false_negatives],
        'Actual Healthy': [false_positives, true_negatives]
    }, index=['Predicted Hypothyroid', 'Predicted Healthy (negative)'])
    st.dataframe(confusion_matrix)

    # Clear the result when the Clear Results button is clicked
    if st.button("Clear Results"):
        st.session_state.dogs_data = None
        st.write("Results cleared. You can sample again.")

else:
    st.write("Click 'Sample Dogs' to generate data and view the plot.")
