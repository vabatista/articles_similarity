import streamlit as st
import numpy as np
import spacy
import json
import faiss


st.title('Article Similarity Search')

st.subheader('This is a demo project to explore concepts of document similarity using vector embeddings.')

n_near_documents = st.text_input("Enter number of documents to return:", "10")
txt_abstract = st.text_area("Enter an article's abstract to search for similar documents","")

with open('./articles.json', 'r') as f:
    parsed_articles = json.load(f)
index = faiss.read_index('./faiss_index.out')
nlp = spacy.load("en_core_web_sm")


if st.button('Search Articles'):
    v = nlp(txt_abstract).vector
    query = np.array([v])

    scores, results = index.search(query, int(n_near_documents))
    frame = [['pos', 'doc_id', 'article', 'vector distance']]
    for i, result in enumerate(results[0]):
        frame.append([str(i+1), str(result), parsed_articles[result]['title'], str(scores[0][i])])    
    st.table(frame)
