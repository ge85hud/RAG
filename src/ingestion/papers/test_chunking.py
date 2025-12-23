from pathlib import Path
from src.ingestion.papers.academic_chunker import chunk_academic_paper


def main():
    project_root = Path(__file__).resolve().parents[3]
    pdf_path = project_root / "data" / "papers" / "sample.pdf"

    docs = chunk_academic_paper(pdf_path)

    print(f"\nTotal chunks: {len(docs)}\n")

    for doc in docs:
        print("=" * 100)
        print(f"SECTION  : {doc['metadata']['section']}")
        print(f"CHUNK ID : {doc['metadata']['chunk_id']}")
        print("-" * 100)
        print(doc["content"])
        print("\n")


if __name__ == "__main__":
    main()