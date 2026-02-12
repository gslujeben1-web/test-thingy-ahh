import streamlit as st

st.title("🔢 Maths Test ➕")
st.title("🟰 Give the answer to each calculation ➗")

st.write("What's your name:")
name = st.text_input("*Name*")

# Create a form
with st.form("math_test_form"):

    # Question 1
    st.write("Find x:")
    st.write("3x − 7 = 2x + 5")
    q1 = st.text_input("Answer 1")

    # Question 2
    st.write("Solve:")
    st.write("x² − 5x + 6 = 0 (give smallest answer)")
    q2 = st.text_input("Answer 2")

    # Question 3
    st.write("Solve the system (value of x):")
    st.write("2x + y = 7")
    st.write("x − y = 1")
    q3 = st.text_input("Answer 3")

    # Question 4
    st.write("Simplify:")
    st.write("(2³ × 2⁴) ÷ 2⁵")
    q4 = st.text_input("Answer 4")

    # Question 5
    st.write("Simplify:")
    st.write("(x² − 9) / (x − 3)")
    q5 = st.text_input("Answer 5")

    # Question 6
    st.write("Find the area of a triangle (base=10, height=6)")
    q6 = st.text_input("Answer 6")

    # Submit button
    submitted = st.form_submit_button("Submit Answers")

# Only check answers AFTER submission
if submitted:

    st.write("### Results")

    if q1 == "12":
        st.write("Q1: ✅ Correct")
    else:
        st.write("Q1: ❌ Incorrect (Correct: 12)")

    if q2 == "2":
        st.write("Q2: ✅ Correct")
    else:
        st.write("Q2: ❌ Incorrect (Correct: 2 or 3)")

    if q3 == "8/3":
        st.write("Q3: ✅ Correct")
    else:
        st.write("Q3: ❌ Incorrect (Correct: 8/3)")

    if q4 == "4":
        st.write("Q4: ✅ Correct")
    else:
        st.write("Q4: ❌ Incorrect (Correct: 4)")

    if q5.replace(" ", ""
