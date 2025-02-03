import streamlit as st
import pandas


st.set_page_config(layout="wide")

col1 , col2 = st.columns(2)

with col1:
    st.image("images/guney.jpeg")

with col2:
    st.title("Guney Dogan")
    content = """
I am a Python developer and data analyst with a Master's in International Business & Entrepreneurship from Lappeenranta University of Technology (LUT), Finland. I specialize in data analysis, automation, and business intelligence using Python. Driven by a passion for data-driven decision-making and problem-solving, I continuously seek to innovate and improve processes. This portfolio showcases my Python projects, demonstrating my ability to extract insights and develop solutions for real-world business challenges.
 """
    st.info(content)


content2 = """
Below you can find some of the apps I have built in Python.
"""
st.write(content2)

col3 , empyt_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for  index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")


with col4:
    for index,row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")