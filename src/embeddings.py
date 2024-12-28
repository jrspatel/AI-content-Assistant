import json
import os
from sentence_transformers import SentenceTransformer
import numpy as np 



def generate_embeddings(text_list):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(text_list, show_progress_bar=True)
    return embeddings




# Load JSON files from a folder
folder_path = "./data"  # Folder containing your JSON files
files = [f for f in os.listdir(folder_path) if f.endswith('.json')]

# Load data into a dictionary
data = {}
for file in files:
    with open(os.path.join(folder_path, file), "r") as f:
        data[file] = json.load(f)



# convert raw text into embeddings
texts_to_embed = []
for file in data:
    texts_to_embed.append(data[file]) 

embeddings = generate_embeddings(texts_to_embed) 
np.save("embeddings.npy", embeddings)
print(f"Embeddings generated and saved! Shape: {embeddings.shape}")

