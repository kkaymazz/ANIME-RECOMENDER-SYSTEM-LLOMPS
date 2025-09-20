import streamlit as st
from pipeline.pipeline import AnimeRecommendationPipeline
from dotenv import load_dotenv

st.set_page_config(page_title="Anime Recommender", layout="wide")

# Force dark theme CSS
st.markdown(
    """
    <style>
    body {
        background-color: #0E1117;
        color: #FAFAFA;
    }
    .stTextInput > div > div > input {
        background-color: #1E222A;
        color: #FAFAFA;
        border-radius: 6px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

load_dotenv()

@st.cache_resource
def init_pipeline():
    return AnimeRecommendationPipeline()

pipeline = init_pipeline()

st.title("🎌 Anime Recommender System")

query = st.text_input("Enter your anime preferences, e.g.: light-hearted anime with school settings")
if query:
    with st.spinner("Fetching recommendations for you....."):
        response = pipeline.recommend(query)
        st.markdown("### Recommendations")
        st.write(response)