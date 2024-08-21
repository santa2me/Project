from PIL import Image
import streamlit as st

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Yugyeong's Webpage", page_icon=":tada:", layout="wide")

# ---- LOAD ASSETS ----
img_book = Image.open("images/IMG_0432.JPG")
img_me = Image.open("images/IMG_1452.PNG")

#---- HEADER SECTION -----

with st.container():
    st.subheader("Hi, I am Yugyeong :wave:")
    st.title("A unemployed developer")
    st.write("I want to do something here")
    st.write("[Learn More >](https://www.webfx.com/tools/emoji-cheat-sheet/)")


#-------

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##########")
    
    with right_column:
        st.header("WHAT AM I DOING")
        st.write("well")


#---- Projects ----
with st.container():
    st.write("-----")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_book)
    
    with text_column:
        st. subheader("it's first image's subheader")

