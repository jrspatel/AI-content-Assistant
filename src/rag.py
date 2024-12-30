import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import tensorflow as tf 
from embeddings import texts_to_embed
from transformers import pipeline 


# Check the number of GPUs available
# gpus = tf.config.experimental.list_physical_devices('GPU')
# if gpus:
#     print(f"GPUs found: {len(gpus)}")
# else:
#     print("No GPU found.")
# qdwwq

# Load embeddings and initialize FAISS
embeddings = np.load("D:/AI-content-Assistant/src/embeddings.npy")
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

model = SentenceTransformer('all-MiniLM-L6-v2')


query = "What is trending in AI?"
query_embedding = model.encode([query])

# Perform FAISS search
D, I = index.search(query_embedding, k=5)  # Retrieve top 5 matches
print("Top Results Indexes:", I)

received_texts = [str(texts_to_embed[i]) for i in I[0]] 



# Initialize GPT summarization model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")




combined_text = " ".join(received_texts)

# Summarize the combined text
max_length = min(200, int(len(combined_text.split()) * 0.8))  # Allow for a rich summary
min_length = max(60, int(len(combined_text.split()) * 0.5))   # Ensure sufficient depth

summary = summarizer(
    combined_text, max_length=max_length, min_length=min_length, do_sample=False
)[0]['summary_text']

# Output the final summary
print("Final Summary for Content Creators:")
print(summary)
