import streamlit as st

st.markdown(
    """
    <style>
    .stApp { background-color: #5B7F70; }
    .stApp, .stApp h1 {font-size: 100px;
        color: #90CEFB;
        text-align: center;}
    .stApp h2, .stApp p {color: #ECB2EA; }
    [data-testid="stImage"] {
        display: flex;
        justify-content: center;
    }
    [data-testid="stImage"] img {
        margin: auto;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("""# Buzz the cat
## Meeting with Buzz the Lightyear
When Buzz meets Buzz.""")

size = st.slider('Adjust the picture size', 100, 800, 400)

st.image("BUZZ.png", caption="Buzz & Buzz", width=size)
