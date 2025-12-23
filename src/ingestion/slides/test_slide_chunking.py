from pathlib import Path
from src.ingestion.slides.persistent_vector_store import ingest_slides


def main():
    project_root = Path(__file__).resolve().parents[3]
    pptx_path = project_root / "data" / "slides" / "sample.pptx"

    if not pptx_path.exists():
        raise FileNotFoundError(f"Slide file not found: {pptx_path}")

    ingest_slides(pptx_path)


if __name__ == "__main__":
    main()