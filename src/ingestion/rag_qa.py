from pathlib import Path
from typing import List, Dict
import json
import numpy as np

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from transformers import pipeline


class KnowledgeBase:
    def __init__(self, store_dir: Path):
        self.vectors = np.load(store_dir / "vectors.npy")
        with open(store_dir / "metadata.json", "r", encoding="utf-8") as f:
            self.metadata = json.load(f)

        self.embedder = SentenceTransformer("all-MiniLM-L6-v2")

    def search(self, query: str, top_k: int = 3) -> List[Dict]:
        query_vector = self.embedder.encode(
            query,
            convert_to_numpy=True,
            normalize_embeddings=True
        )

        scores = cosine_similarity(
            query_vector.reshape(1, -1),
            self.vectors
        )[0]

        top_indices = np.argsort(scores)[::-1][:top_k]

        results = []
        for idx in top_indices:
            results.append({
                "score": float(scores[idx]),
                "content": self.metadata[idx]["content"],
                "metadata": self.metadata[idx]["metadata"]
            })

        return results


class RAGQA:
    def __init__(self):
        self.llm = pipeline(
            "text2text-generation",
            model="google/flan-t5-base",
            max_length=512
        )

    def generate_answer(self, question: str, contexts: List[str]) -> str:
        context_text = "\n\n".join(
            [f"Context {i+1}: {ctx}" for i, ctx in enumerate(contexts)]
        )

        prompt = f"""
You are an academic assistant.

Answer the question using ONLY the provided context.
If the answer is not in the context, say "I don't know".

{context_text}

Question: {question}
Answer:
"""

        response = self.llm(prompt)[0]["generated_text"]
        return response.strip()