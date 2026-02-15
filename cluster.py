import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

# Read log file
with open("logs.txt", "r") as file:
    logs = file.readlines()

# Convert text to TF-IDF features
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(logs)

# Apply KMeans clustering
kmeans = KMeans(n_clusters=2, random_state=42)
kmeans.fit(X)

# Create output directory if not exists
os.makedirs("output", exist_ok=True)

# Save results
df = pd.DataFrame({
    "log": logs,
    "cluster": kmeans.labels_
})

df.to_csv("output/clustered_logs.csv", index=False)

print("Clustering completed successfully!")
