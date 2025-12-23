from pathlib import Path

from src.ingestion.slides.slide_chunker import extract_slides
from src.ingestion.slides.slide_embedding import SlideEmbedding


def main():
    # Resolve project root
    project_root = Path(__file__).resolve().parents[3]

    # Real PPT file
    pptx_path = project_root / "data" / "ppt" / "sample.pptx"

    if not pptx_path.exists():
        raise FileNotFoundError(f"PPT file not found: {pptx_path}")

    # 1️⃣ Load existing slide chunks (chunking already implemented elsewhere)
    slide_chunks = extract_slides(pptx_path)
    print(f"Slide chunks extracted: {len(slide_chunks)}")

    # 2️⃣ Embed + save vectors
    embedder = SlideEmbedding()
    embedded_chunks = embedder.embed(slide_chunks)

    # 3️⃣ Verification output
    print(f"Embedded chunks saved: {len(embedded_chunks)}")
    print("Embedding vector shape:", embedded_chunks[0]["embedding"].shape)
    print("Last embedded metadata:", embedded_chunks[-1]["metadata"])


if __name__ == "__main__":
    main()