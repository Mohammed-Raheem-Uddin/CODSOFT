import streamlit as st
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b == 0:
        return "'Sorry not defined'"
    return a/b
def calculator():
    st.title("Simple Calculator")
    st.write("** Calculator for basic arithmetic operations **")
    num1 = st.number_input("Enter first number: ",step=1.0)
    num2 = st.number_input("Enter second number: ", step=1.0)
    operator = st.selectbox("Select an operator:",("+","-","*","/"))
    result = 0
    if operator == "+":
        result = add(num1,num2)
    elif operator == "-":
        result = sub(num1,num2)
    elif operator == "*":
        result = multiply(num1,num2)
    elif operator == "/":
        result = divide(num1,num2)
    st.write("The result is:",result)

if __name__ =='__main__':
    calculator()
