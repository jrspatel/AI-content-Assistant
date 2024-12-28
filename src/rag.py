import faiss

# Load embeddings
embeddings = np.load("embeddings.npy")

# Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)  # L2 distance metric
index.add(embeddings)

# Query (example)
query_embedding = model.encode(["What is trending in AI?"])
D, I = index.search(query_embedding, k=5)  # Top 5 results

# Display results
print("Top Results:", I)
