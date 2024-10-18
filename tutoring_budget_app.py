import streamlit as st

# Function to calculate total cost of tutoring
def calculate_total_cost(num_students, num_weeks, num_classes, hourly_wage):
    # Total number of hours for all students (1 hour per week per class)
    total_hours = num_students * num_weeks * num_classes  # Removed the 5 hours per week assumption
    # Total cost for all the tutoring hours
    total_cost = total_hours * hourly_wage
    return total_cost

# Streamlit UI with larger text size using Markdown and HTML
st.markdown("<h1 style='text-align: center; font-size: 48px;'>Tutoring Program Budget Calculator</h1>", unsafe_allow_html=True)

# Sliders for user input with labels in larger text
st.markdown("<h3 style='font-size: 24px;'>Number of students receiving tutoring</h3>", unsafe_allow_html=True)
num_students = st.slider("", min_value=1, max_value=10, value=5, step=1)

st.markdown("<h3 style='font-size: 24px;'>Number of weeks of tutoring</h3>", unsafe_allow_html=True)
num_weeks = st.slider("", min_value=1, max_value=30, value=8, step=1)

st.markdown("<h3 style='font-size: 24px;'>Number of classes receiving tutoring (1 - 3)</h3>", unsafe_allow_html=True)
num_classes = st.slider("", min_value=1, max_value=3, value=1, step=1)

st.markdown("<h3 style='font-size: 24px;'>Hourly wage of tutors ($)</h3>", unsafe_allow_html=True)
hourly_wage = st.slider("", min_value=10, max_value=100, value=25, step=1)

# Input for total budget
st.markdown("<h3 style='font-size: 24px;'>Enter your total available budget ($)</h3>", unsafe_allow_html=True)
budget = st.number_input("", min_value=0, value=10000)

# Calculate total cost
total_cost = calculate_total_cost(num_students, num_weeks, num_classes, hourly_wage)

# Display the total cost with larger text
st.markdown(f"<h3 style='font-size: 24px;'>Total cost for the tutoring program: <strong>${total_cost:.2f}</strong></h3>", unsafe_allow_html=True)

# Comparison with budget in larger text
if total_cost <= budget:
    st.markdown(f"<h3 style='color: green; font-size: 24px;'>The tutoring program is within the budget. You will have <strong>${budget - total_cost:.2f}</strong> left.</h3>", unsafe_allow_html=True)
else:
    st.markdown(f"<h3 style='color: red; font-size: 24px;'>The tutoring program exceeds the budget by <strong>${total_cost - budget:.2f}</strong>.</h3>", unsafe_allow_html=True)
