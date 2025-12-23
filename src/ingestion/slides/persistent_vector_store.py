from pathlib import Path
from typing import List, Dict
import numpy as np


class PersistentVectorStore:
    """
    Append-only vector store for papers + slides.
    """

    def __init__(self, store_dir: Path):
        self.store_dir = store_dir
        self.store_dir.mkdir(parents=True, exist_ok=True)

        self.embeddings_path = self.store_dir / "embeddings.npy"
        self.metadata_path = self.store_dir / "metadata.npy"
        self.chunks_path = self.store_dir / "chunks.npy"

        self.embeddings = self._load_embeddings()
        self.metadata = self._load_metadata()
        self.chunks = self._load_chunks()

    def _load_embeddings(self) -> np.ndarray:
        if self.embeddings_path.exists():
            return np.load(self.embeddings_path)
        return np.empty((0, 384))  # MiniLM dimension

    def _load_metadata(self) -> List[Dict]:
        if self.metadata_path.exists():
            return np.load(self.metadata_path, allow_pickle=True).tolist()
        return []

    def _load_chunks(self) -> List[Dict]:
        if self.chunks_path.exists():
            return np.load(self.chunks_path, allow_pickle=True).tolist()
        return []

    def add(self, embedded_chunks: List[Dict]):
        if not embedded_chunks:
            return

        new_embeddings = np.vstack([c["embedding"] for c in embedded_chunks])
        new_chunks = [{"content": c["content"], "metadata": c["metadata"]}
                      for c in embedded_chunks]
        new_metadata = [c["metadata"] for c in embedded_chunks]

        self.embeddings = np.vstack([self.embeddings, new_embeddings])
        self.chunks.extend(new_chunks)
        self.metadata.extend(new_metadata)

        self._save()

    def _save(self):
        np.save(self.embeddings_path, self.embeddings)
        np.save(self.chunks_path, np.array(self.chunks, dtype=object))
        np.save(self.metadata_path, np.array(self.metadata, dtype=object))