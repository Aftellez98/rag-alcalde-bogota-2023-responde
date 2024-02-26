import os

# -----------------
# Load data
# -----------------

from langchain.document_loaders import PyPDFLoader

def load_data(pdf_path):
    
    # Import the program (PDF) to python using langchain
    loader = PyPDFLoader(pdf_path)
    pages = loader.load()

    return pages

# -----------------
# Creating the splitting object based on paragraphs and sentences
# -----------------

from langchain.text_splitter import RecursiveCharacterTextSplitter

def splitter(pdf_path):

    pages = load_data(pdf_path)

    r_splitter = RecursiveCharacterTextSplitter(
        chunk_size=2000,
        chunk_overlap=0,
        separators=["\n\n\n", "\n\n", "(?<=\.)"])

    splits = r_splitter.split_documents(pages)

    return splits

# -----------------
# Create the embedding object
# -----------------

from langchain.embeddings.openai import OpenAIEmbeddings

def embedding_generator(splits):
    embedding = OpenAIEmbeddings()
    return [embedding.embed_query(split.page_content) for split in splits]

# -----------------
# Store embeddings
# -----------------

import csv

def store_embedding(candidate, embeddings):
    with open(candidate + '.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(embeddings)

def store_splits(candidate, splits):
    with open(candidate + '.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for split in splits:
            writer.writerow([split])

# -----------------
# Convert item into a double
# -----------------

def convert_to_number(item):
    try:
        return int(item)
    except ValueError:
        try:
            return float(item)
        except ValueError:
            return item
        
# -----------------
# Reading embedding
# -----------------

def read_embedding(candidate):
    with open(candidate + '.csv', 'r') as file:
        reader = csv.reader(file)
        embedding = []
        for row in reader:
            embedding.append([convert_to_number(item) for item in row])
    
    return embedding

