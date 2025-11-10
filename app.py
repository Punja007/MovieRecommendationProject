import pickle
import pandas as pd
import streamlit as st

#loading the datas from ipynb file
df = pickle.load(open('data_to_dict.pkl',mode='rb'))
df = pd.DataFrame(df)

similarity = data = pickle.load(open('similarity.pkl',mode='rb'))

def recommend(movie):
    recommended = []
    #fetching index
    mv_index = df[df['title'] == movie].index[0]

    #gets a list of top 5 movies
    top5_list = (sorted(enumerate(list(similarity[mv_index])),reverse=True,key=lambda x: x[1])[1:6])

    for i in top5_list:
        recommended.append(df.iloc[i[0]].title)

    return recommended




##streamLit Web App
st.title('Movie :blue[Recommendation] Model')
st.divider()
selected_movie = st.selectbox('Select your Movie',df['title'].values)
btn = st.button(label="Recommend")

if btn:
    recommended_movies = recommend(selected_movie)
    
    for i in recommended_movies:
        st.subheader(i)
