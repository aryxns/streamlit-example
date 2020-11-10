import streamlit as st
import hnpy
import requests


hn = hnpy.HackerNews()
st.title("HN Browser")

menu = ["Home","Show", "Jobs", "Posts"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Home":
    st.header("Welcome to HN Browser")
    st.write("--------------------------------------")
    st.markdown("HN Browser allows you to get the best of Hacker News with a **simplified UI** with added **functionality.**")
elif choice == "Show":
    st.subheader("HN Show")
    st.write("----------------------------------")
    query = st.sidebar.text_input("Search: ")
    if st.sidebar.button("Show"):
        for post in hn.show(limit=5):
            if str(query) in str(post.title):
                st.write(post.title) 
                st.write(post.content)
                st.write("----------------------------------")
    elif st.sidebar.button("Latest"):
        for post in hn.show(limit=5):
            st.write(post.title)
            if len(post.content) < 500:
                    st.write(post.content)
            elif len(post.content) > 500:
                    st.write(post.link)
            st.write("----------------------------------")

elif choice == "Jobs":
    st.subheader("Job Index")
    st.write("----------------------------------")
    role = st.sidebar.text_input("Enter role: ")
    if st.sidebar.button("Load Jobs"):
        for post in hn.jobs(limit=10):
            if str(role) in str(post.title):
                st.write(post.title)
                st.write(post.content)
                st.write("----------------------------------")
                
elif choice == "Posts":
    st.subheader("Post Section")
    st.write("----------------------------------")
    query = st.sidebar.text_input("Search for a post: ")
    if st.sidebar.button("Search"):
        for post in hn.top():
            if str(query) in str(post.title):
                st.write(post.title)
                st.write(post.link)
                st.write()

    elif st.sidebar.button("Latest Posts"):
        for post in hn.top(limit=5):
            st.write(post.title + " " + post.link)
            st.write("----------------------------------")
    elif st.sidebar.button("Best Posts"):
        for post in hn.best(limit=5):
            st.write(post.title)
            st.write(post.link)
            st.write("----------------------------------")
                


hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
