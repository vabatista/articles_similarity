# Scientific articles similarity demo
Demo for indexing scientific articles in PDF and search for similarity between them.
I decided to use a Vector representation of each document, using Word2Vec average of each token inside document. 

The notebooks folder contains scripts to load, parse and index articles, producing `articles.json` and `faiss_index.out`.

# Config
1 - Create a conda env using pre-reqs.
> conda env create -f environment.yml
> 
> conda activate articles_similarity

2 - If you want to run the pdf parse notebook, you must run the server:
> bash serve_grobid.sh

3 - Run the Streamlit app
> streamlit run streamlit_frontend.py
