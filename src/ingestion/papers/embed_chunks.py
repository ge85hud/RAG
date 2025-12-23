from typing import List, Dict
import numpy as np
from sentence_transformers import SentenceTransformer


class ChunkEmbedder:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def embed_chunks(self, chunks: List[Dict]) -> List[Dict]:
        """
        Embed chunk content and attach vectors to each chunk.
        """
        texts = [chunk["content"] for chunk in chunks]

        embeddings = self.model.encode(
            texts,
            show_progress_bar=True,
            convert_to_numpy=True,
            normalize_embeddings=True
        )

        embedded_chunks = []
        for chunk, vector in zip(chunks, embeddings):
            embedded_chunks.append({
                "content": chunk["content"],
                "metadata": chunk["metadata"],
                "embedding": vector
            })

        return embedded_chunks