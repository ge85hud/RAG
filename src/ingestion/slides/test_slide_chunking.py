from pathlib import Path
from src.ingestion.slides.slide_chunker import extract_slides


def main():
    project_root = Path(__file__).resolve().parents[3]
    pptx_path = project_root / "data" / "slides" / "sample.pptx"

    if not pptx_path.exists():
        raise FileNotFoundError(f"Missing slide file: {pptx_path}")

    chunks = extract_slides(pptx_path)

    print(f"\nTotal slides extracted: {len(chunks)}\n")

    for chunk in chunks:
        print("=" * 80)
        print(f"Slide #: {chunk['metadata']['slide_number']}")
        print(chunk["content"])
        print()


if __name__ == "__main__":
    main()
