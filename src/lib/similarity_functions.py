# -----------------
# SIMILARITY
# -----------------

from langchain.embeddings.openai import OpenAIEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np
import openai
import os

openai.api_key = os.environ['OPENAI_API_KEY']

# -----------------
# Dot product
# -----------------

def dot_product(question, embeddings):
    embedding = OpenAIEmbeddings()
    embedding_question = embedding.embed_query(question)
    return [np.dot(embedding, embedding_question) for embedding in embeddings]

# -----------------
# Cosine Distance
# -----------------

def cosine_distance(question, embeddings):
    embedding = OpenAIEmbeddings()
    embedding_question = embedding.embed_query(question)
    return [cosine_similarity([embedding], [embedding_question])[0, 0] for embedding in embeddings]

# -----------------
# Dataframe
# -----------------

def dataframe(splits, dot_product):

    #Initializing the df
    df = pd.DataFrame([])

    # Adding columns to the df
    df["content"] = splits
    df["distance"] = dot_product

    return df