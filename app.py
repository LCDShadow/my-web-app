import streamlit as st

st.set_page_config(page_title="мое супер приложение", page_icon="🐽", layout="wide")

st.title("добро пожаловать на мое приложение 🤙")

tab1, tab2 = st.tabs(["про меня", "мои инструменты"])

with tab1:
    st.header("ознакомление с автором")
    col1, col2 = st.columns([1,2])
    with col1:
        st.image("https://imgs.search.brave.com/PBpVrM6ti2TAeQ_9Aa-yey8EBw-5r92NSfiKcXFKOyk/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9rYXJ0/aW5rb2YuY2x1Yi91/cGxvYWRzL3Bvc3Rz/LzIwMjItMDMvdGh1/bWJzLzE2NDg2ODU4/MDVfMzAta2FydGlu/a29mLWNsdWItcC1r/YXJ0aW5raS1zbWVz/aG5pZS16aGR1bmEt/MzAucG5nv")
        with col2:
            st.subheader("привет я кто-то ")
            st.write("я учусь где-то")
