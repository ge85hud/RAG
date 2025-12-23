from typing import List, Dict
from pathlib import Path

from sentence_transformers import SentenceTransformer
from src.ingestion.papers.persistent_vector_store import PersistentVectorStore


class SlideEmbedding:
    """
    Embed slide chunks and persist vectors.
    """

    def __init__(
        self,
        model_name: str = "all-MiniLM-L6-v2",
        store_dir: Path | None = None
    ):
        self.model = SentenceTransformer(model_name)

        if store_dir is None:
            project_root = Path(__file__).resolve().parents[3]
            store_dir = project_root / "data" / "vector_store" / "index"

        self.store = PersistentVectorStore(store_dir)

    def embed(self, slide_chunks: List[Dict]) -> List[Dict]:
        """
        Embed slide chunks and save them.
        """
        texts = [chunk["content"] for chunk in slide_chunks]

        embeddings = self.model.encode(
            texts,
            show_progress_bar=True,
            convert_to_numpy=True,
            normalize_embeddings=True
        )

        embedded_chunks = []
        for chunk, vector in zip(slide_chunks, embeddings):
            embedded_chunks.append({
                "content": chunk["content"],
                "metadata": chunk["metadata"],
                "embedding": vector
            })

        # Save vectors + chunks (append-only)
        self.store.add(embedded_chunks)

        return embedded_chunks