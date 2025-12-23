from pathlib import Path
from src.ingestion.papers.academic_chunker import chunk_academic_paper
from src.ingestion.papers.embed_chunks import ChunkEmbedder
from src.ingestion.papers.persistent_vector_store import PersistentVectorStore



def main():
    project_root = Path(__file__).resolve().parents[3]

    pdf_path = project_root / "data" / "papers" / "sample.pdf"
    store_dir = project_root / "data" / "vector_store" / "index"

    # 1. Chunk
    chunks = chunk_academic_paper(pdf_path)
    print(f"Chunks created: {len(chunks)}")

    # 2. Embed
    embedder = ChunkEmbedder()
    embedded_chunks = embedder.embed_chunks(chunks)

    # 3. Append to vector store
    store = PersistentVectorStore(store_dir)
    store.add(embedded_chunks)

    print(f"Total vectors in KB: {len(store.metadata)}")


if __name__ == "__main__":
    main()