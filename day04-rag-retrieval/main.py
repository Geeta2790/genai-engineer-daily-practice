from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Step 1: Sample corpus
documents = [
    "Python is a popular programming language used in data science and web development.",
    "FastAPI is a modern web framework for building APIs with Python.",
    "LangGraph helps build stateful agent workflows using graphs.",
    "Retrieval Augmented Generation combines retrieval with language models.",
    "Redis is an in-memory data store used for caching and message queues.",
    "Docker allows packaging applications into portable containers.",
    "Pytest is a testing framework that makes it easy to write small tests in Python.",
]


# Step 2: Split a long text into chunks of N words
def split_into_chunks(text, chunk_size=20):
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size):
        chunks.append(" ".join(words[i:i + chunk_size]))
    return chunks


# Step 3: Build the TF-IDF index over the corpus
vectorizer = TfidfVectorizer(stop_words="english", lowercase=True)
doc_vectors = vectorizer.fit_transform(documents)


# Step 4: Retrieve top-k relevant chunks for a query
def retrieve(query, top_k=3):
    query_vector = vectorizer.transform([query])
    similarities = cosine_similarity(query_vector, doc_vectors).flatten()
    top_indices = similarities.argsort()[::-1][:top_k]

    results = []
    for idx in top_indices:
        results.append({
            "document": documents[idx],
            "score": float(similarities[idx]),
        })
    return results


# Step 5: Run a few example queries
if __name__ == "__main__":
    queries = [
        "How do I build an API in Python?",
        "What is used for caching?",
        "Tell me about agent workflows",
    ]

    for query in queries:
        print(f"\nQuery: {query}")
        results = retrieve(query, top_k=2)
        for i, r in enumerate(results, 1):
            print(f"  {i}. [score={r['score']:.3f}] {r['document']}")
