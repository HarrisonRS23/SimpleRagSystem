# convert each chunk into an embedding vector, 
# then store the chunk and its corresponding vector in a list.
# example for calculate the embedding vector for a given text:

import ollama

# ollama models 
EMBEDDING_MODEL = 'hf.co/CompendiumLabs/bge-base-en-v1.5-gguf'
LANGUAGE_MODEL = 'hf.co/bartowski/Llama-3.2-1B-Instruct-GGUF'
dataset = []




# Implement Vector Database  ***********

# Each element in the VECTOR_DB will be a tuple (chunk, embedding)
# The embedding is a list of floats, for example: [0.1, 0.04, -0.34, 0.21, ...]
VECTOR_DB = []

# Each line is a chunk for simplicity
# add each chunk to the "database" using embedding model 
# vector_db is a list of chunks represented as vectors 
def add_chunk_to_database(chunk):
  embedding = ollama.embed(model=EMBEDDING_MODEL, input=chunk)['embeddings'][0]
  VECTOR_DB.append((chunk, embedding))


# Retrieval functions ***************

# Cosine similirity algorithm between two vectors (implementing retrieval function)
# higher the cosine similarity indicates vectors are "closer" in vector space 
def cosine_similarity(a, b):
  dot_product = sum([x * y for x, y in zip(a, b)])
  norm_a = sum([x ** 2 for x in a]) ** 0.5
  norm_b = sum([x ** 2 for x in b]) ** 0.5
  return dot_product / (norm_a * norm_b)

def retrieve(query, top_n=3):
  query_embedding = ollama.embed(model=EMBEDDING_MODEL, input=query)['embeddings'][0]
  # temporary list to store (chunk, similarity) pairs
  similarities = []
  for chunk, embedding in VECTOR_DB:
    similarity = cosine_similarity(query_embedding, embedding)
    similarities.append((chunk, similarity))
  # sort by similarity in descending order, because higher similarity means more relevant chunks
  similarities.sort(key=lambda x: x[1], reverse=True)
  # finally, return the top N most relevant chunks
  return similarities[:top_n]



def main():
    # load cat dataset into a list of strings 
    with open('cat.txt', 'r') as file:
        dataset = file.readlines()
    # successfull loading of dataset
    print(f'Loaded {len(dataset)} entries')

    # add each chunk to the database from the cat dataset
    for i, chunk in enumerate(dataset):
        add_chunk_to_database(chunk)
    print(f'Added chunk {i+1}/{len(dataset)} to the database')


if __name__ == "__main__":
    main()
