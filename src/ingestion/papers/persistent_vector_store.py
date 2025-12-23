from pathlib import Path
from typing import List, Dict
import json
import numpy as np


class PersistentVectorStore:
    def __init__(self, store_dir: Path):
        self.store_dir = store_dir
        self.store_dir.mkdir(parents=True, exist_ok=True)

        self.vectors_path = self.store_dir / "vectors.npy"
        self.metadata_path = self.store_dir / "metadata.json"
        self.state_path = self.store_dir / "index_state.json"

        self._load_or_initialize()

    def _load_or_initialize(self):
        if self.vectors_path.exists():
            self.vectors = np.load(self.vectors_path)
            with open(self.metadata_path, "r", encoding="utf-8") as f:
                self.metadata = json.load(f)
        else:
            self.vectors = np.empty((0, 384), dtype="float32")
            self.metadata = []

        self._save_state()

    def _save_state(self):
        with open(self.state_path, "w") as f:
            json.dump(
                {
                    "total_vectors": len(self.metadata)
                },
                f,
                indent=2
            )

    def add(self, embedded_chunks: List[Dict]):
        new_vectors = np.array(
            [chunk["embedding"] for chunk in embedded_chunks],
            dtype="float32"
        )

        self.vectors = np.vstack([self.vectors, new_vectors])

        for chunk in embedded_chunks:
            self.metadata.append({
                "content": chunk["content"],
                "metadata": chunk["metadata"]
            })

        self.save()

    def save(self):
        np.save(self.vectors_path, self.vectors)
        with open(self.metadata_path, "w", encoding="utf-8") as f:
            json.dump(self.metadata, f, indent=2)

        self._save_state()