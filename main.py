import streamlit as st

st.title("🔢Maths Test➕")
st.title("🟰Give the answer to each calculation➗")

st.write("Whats your name:")
name = st.text_input("*name*")

st.write("find x:\n3x−7=2x+5")
q1 = st.number_input("type the Answer")

if q1 == 12:
  st.write("✅Correct✅")
else:
  st.write("❌Incorrect❌\nThe Right answer is 12")
