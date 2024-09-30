# streamlit run Calculator.py 
import streamlit as st

# Title of the app
st.title("Simple Calculator")

# input number
num1 = st.number_input("Enter the first number")
num2 = st.number_input("Enter the second number")

# select operation
operation = st.selectbox("Select operation", ["Add", "Subtract", "Multiply", "Divide"])

if operation == "Add":
    result = num1 + num2
elif operation == "Subtract":
    result = num1 - num2
elif operation == "Multiply":
    result = num1 * num2
elif operation == "Divide":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Number 2 cannot be zero for division operation"

st.write(f"Result: {result}")