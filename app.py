import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate( distances)),reverse=True,key=lambda x:x[1])[1:6]

    recommended_movies=[]


    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies=pd.DataFrame(movies_dict)

similarity=pickle.load(open('similarity.pkl', 'rb'))
st.title("Movie-Recommendor-System")

selected_movies_name=st.selectbox(
    "Here are your movie picks",
    movies['title'].values)


page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-color: #1e1e2f; /* Dark purple/blue */
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1524985069026-dd778a71c7b4");
    background-size: cover;
}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

if st.button("Explore"):
    recommendation=recommend(selected_movies_name)
    for i in recommendation:
        st.write(i)