import streamlit as st
import pandas as pd

# title
st.title("This is Streamlit Widget")

# taking input
name=st.text_input("Enter your Name:")

# displaying the name
if name:
    st.write(f"Hello {name}")

# taking age input from a slider
age=st.slider("Select your age:",0,100,18)
st.write(f"Your age is : {age}")

# choosing the user's favorite language using selectbox
options=['C','C++','Java','Python','HTML','Javascript']
choice=st.selectbox("Choose your preffered language: ",options)
if choice:
    st.write(f"Your language is {choice}")

# displaying a dataframe
data=pd.DataFrame(
    {
        'Name':['Han','Aditya','Bhelteshwar','Swihan','Chomander'],
        'Age':[20,19,24,37,23],
        'City':['Maderia','Manchester','Madrid','Turin','Mumbai']
    }
)
st.write(data)

# uploading files 
file=st.file_uploader("Upload a CSV File",type="CSV")
if file is not None:
    df=pd.read_csv(file)
    st.write(df.head(10))