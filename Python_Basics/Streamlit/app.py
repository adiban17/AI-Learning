import streamlit as st
import numpy as np
import random
import pandas as pd

# Title of the app
st.title("Hello Streamlit")

# Writing text on streamlit
st.write("This is my Streamlit App!")

# Creating a DataFrame
st.write("This is a DataFrame")
df=pd.DataFrame({'columns':[1,2,3,4,5], 'rows':['a','b','c','d','e']})

# displaying the datagrame on the app
st.write(df)

# creating a line chart
st.write("This is a line chart")
rand_ints=[]
for x in range(0,5):
    num=random.randint(1,11)
    rand_ints.append(num)
y_axis=[12,34,45,67,78]
st.line_chart(pd.DataFrame(rand_ints,y_axis))
