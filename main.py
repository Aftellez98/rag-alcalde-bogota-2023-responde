'''
Manual - RAG
'''

import pandas as pd
import os

from langchain.llms import OpenAI
from langchain.output_parsers import CommaSeparatedListOutputParser
from langchain.prompts import PromptTemplate

from src.lib.lm import get_completion
from src.lib.similarity_functions import dot_product, cosine_distance, dataframe

## ------------------
# USER INPUT
## ------------------
pregunta = input('Insert question:')

## ------------------
## 1. IDENTIFY THE CANDIDATES THE QUESTION REFERS TOO
## ------------------

# Parser -> Lista de candidatos 
output_parser = CommaSeparatedListOutputParser()

format_instructions = output_parser.get_format_instructions()

# Prompt
prompt = PromptTemplate(
    template="Identifica de la siguiente pregunta a los candidatos: {question}. Solo incluye a los que aprezcan aquí: [\"Carlos_Galan\", \"Diego_Molano\", \"Gustavo_Bolivar\", \"Jorge_Luis_Vargas\", \"Jorge_Robledo\", \"Juan_Daniel_Oviedo\", \"Nicolas_Ramos\", \"Rodrigo_Lara\"].\n{format_instructions}",
    input_variables=["question"],
    partial_variables={"format_instructions": format_instructions}
)

# Formatear la pregunta a un objeto que pueda recibir el modelo
_input = prompt.format(question=pregunta)

# Crear objeto con modelo
model = OpenAI(temperature=0)

# Correr el model
output = model(_input)

# Convertir respuesta a tipo lista
candidate_list = output_parser.parse(output)

# Filtrar de modo que solo aparezcan aquellos candidatos que fueron creados de forma correcta
original_names = ["Carlos_Galan", "Diego_Molano", "Gustavo_Bolivar", "Jorge_Luis_Vargas", "Jorge_Robledo", "Juan_Daniel_Oviedo", "Nicolas_Ramos", "Rodrigo_Lara"]
candidates = [name for name in candidate_list if name in original_names]

print("----THE SELECTED CANDIDATES ARE:-----")
print(candidates)


## ------------------
# RAG 
## ------------------

# Encontar el path hacia la informacion de los candidatos
current_directory = os.getcwd()

# Crear el string con la informacion de los candidatos.
result_string = ""

for candidate in candidates:
    
    # Creating path to splits
    splits_path = os.path.join(current_directory, "src", "content", "splits", candidate + ".csv")
    splits = pd.read_csv(splits_path, header=None)
    splits = splits.values.tolist()
    splits = [split[0] for split in splits]

    # Creating path to embeddings
    embeddings_path = os.path.join(current_directory, "src", "content", "embeddings", candidate + ".csv")
    embeddings = pd.read_csv(embeddings_path, header=None)
    embeddings = embeddings.values.tolist()

    # Creating a dataframe with dot_product, and the splits
    product = cosine_distance(pregunta, embeddings)
    df = dataframe(splits, product)

    sorted_df = df.sort_values(by='distance', ascending=False)
    content = sorted_df.head()

    content1 = content.iloc[0][0]
    content2 = content.iloc[1][0]
    content3 = content.iloc[2][0]
    content4 = content.iloc[3][0]

    # Assuming `content1`, `content2`, `content3`, `content4` are paragraphs
    candidate_string = f"Candidate: {candidate}\n\n"
    candidate_string += f"Parrafo1: {content1}\n"
    candidate_string += f"Parrafo2: {content2}\n"
    candidate_string += f"Parrafo3: {content3}\n"

    # Append the candidate's string to the overall result
    result_string += candidate_string + "\n"

prompt_template = f"En Colombia hay elecciones para la alcaldía de Bogota. \
        Hay varios candidatos y vas a ayudar a responder sobre lo que piensan. \
        La pregunta es: {pregunta}. \
        Los parrafos del programa de gobierno que contienen la respuests son: {candidates}."

response = get_completion(prompt_template, model="gpt-3.5-turbo")

print(response)

    # print("\n")
    # print("---------------------------------------")
    # print("-----------------EVIDENCE 1----------------------")
    # print("---------------------------------------")
    # print(content1)
    # print("\n")
    # print("---------------------------------------")
    # print("-----------------EVIDENCE 2----------------------")
    # print("---------------------------------------")
    # print(content2)
    # print("\n")
    # print("---------------------------------------")
    # print("-----------------EVIDENCE 3----------------------")
    # print("---------------------------------------")
    # print(content3)