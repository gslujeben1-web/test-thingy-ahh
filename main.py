import streamlit as st

st.title("🔢 Maths Test ➕")
st.title("🟰 Give the answer to each calculation ➗")

st.write("What's your name:")
name = st.text_input("*Name*")

# Question 1
st.write("Find x:")
st.write("3x − 7 = 2x + 5")
q1 = st.text_input("Answer 1")
if q1 == "12":
    st.write("✅ Correct")
else:
    st.write("❌ Incorrect — Correct answer is 12")

# Question 2
st.write("Solve:")
st.write("x² − 5x + 6 = 0 (give smallest answer)")
q2 = st.text_input("Answer 2")
if q2 == "2":
    st.write("✅ Correct")
else:
    st.write("❌ Incorrect — Correct answer is 2 (or 3)")

# Question 3
st.write("Solve the system (value of x):")
st.write("2x + y = 7")
st.write("x − y = 1")
q3 = st.text_input("Answer 3")
if q3 == "8/3":
    st.write("✅ Correct")
else:
    st.write("❌ Incorrect — Correct answer is 8/3")

# Question 4
st.write("Simplify:")
st.write("(2³ × 2⁴) ÷ 2⁵")
q4 = st.text_input("Answer 4")
if q4 == "4":
    st.write("✅ Correct")
else:
    st.write("❌ Incorrect — Correct answer is 4")

# Question 5
st.write("Simplify:")
st.write("(x² − 9) / (x − 3)")
q5 = st.text_input("Answer 5")
if q5 == "x+3":
    st.write("✅ Correct")
else:
    st.write("❌ Incorrect — Correct answer is x+3")

# Question 6
st.write("Find the area of a triangle (base=10, height=6)")
q6 = st.text_input("Answer 6")
if q6 == "30":
    st.write("✅ Correct")
else:
    st.write("❌ Incorrect — Correct answer is 30")

# Question 7
st.write("What is a rational number?")
q7 = st.text_input("Answer 7")
if "fraction" in q7.lower():
    st.write("✅ Acceptable answer")
else:
    st.write("❌ A rational number can be written as a fraction")

# Question 8
st.write("State the Pythagorean Theorem:")
q8 = st.text_input("Answer 8")
if "a^2+b^2=c^2" in q8.replace(" ", "").lower():
    st.write("✅ Correct")
else:
    st.write("❌ Correct answer: a² + b² = c²")

# Question 9
st.write("Derivative of x^n:")
q9 = st.text_input("Answer 9")
if "nx" in q9.lower():
    st.write("✅ Correct")
else:
    st.write("❌ Correct answer: nx^(n-1)")

# Question 10
st.write("What is the mean?")
q10 = st.text_input("Answer 10")
if "average" in q10.lower():
    st.write("✅ Correct")
else:
    st.write("❌ Mean is the average")
