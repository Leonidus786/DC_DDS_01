<<<<<<< HEAD
import streamlit as st
import pandas as pd
import numpy as np

## Title of the aplication
st.title("Hello, learners welcome to the world of Streamlit.")

## Diplay a Simple Text
st.write("This is how you can write anything in streamlit.")

##create a simple Dataframe

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})


# ## Display the Dataframe
st.write("This is the dataframe")
st.write(df)


# ##create a line chart

chart_data=pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
=======
import streamlit as st
import pandas as pd
import numpy as np

## Title of the aplication
st.title("Hello, learners welcome to the world of Streamlit.")

## Diplay a Simple Text
st.write("This is how you can write anything in streamlit.")

##create a simple Dataframe

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})


# ## Display the Dataframe
st.write("This is the dataframe")
st.write(df)


# ##create a line chart

chart_data=pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
>>>>>>> 2146a209 (Local)
st.line_chart(chart_data)