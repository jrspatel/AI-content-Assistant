import json
import os
from sentence_transformers import SentenceTransformer
import numpy as np

def generate_embeddings(text_list, model_name='all-MiniLM-L6-v2'):
    """Generate embeddings for a list of texts."""
    model = SentenceTransformer(model_name)
    embeddings = model.encode(text_list, show_progress_bar=True)
    return embeddings

# Load JSON files from a folder
folder_path = "./data"  # Folder containing your JSON files
files = [f for f in os.listdir(folder_path) if f.endswith('.json')]
print(files)
# Extract text data from JSON
texts_to_embed = []
for file in files:
    with open(os.path.join(folder_path, file), "r") as f:
        try:
            content = json.load(f)
            # Assuming relevant text is in a specific key, e.g., 'text'
            if isinstance(content, dict):
                # Create a combined string by iterating over all key-value pairs
                combined_text = ", ".join([f"{key}: {value}" for key, value in content.items()])
                texts_to_embed.append(combined_text)
            # Adjust key as needed
            elif isinstance(content, list):
                texts_to_embed.extend(content)  # Flatten list of texts
        except json.JSONDecodeError as e:
            print(f"Error reading {file}: {e}")


# Generate embeddings
if texts_to_embed:
    embeddings = generate_embeddings(texts_to_embed)
    # Save embeddings to a file
    np.save("embeddings.npy", embeddings)
    print(f"Embeddings generated and saved! Shape: {embeddings.shape}")
else:
    print("No valid text data found in JSON files.")
