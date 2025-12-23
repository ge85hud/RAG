from pathlib import Path
from src.ingestion.rag_qa import KnowledgeBase, RAGQA


def main():
    project_root = Path(__file__).resolve().parents[2]
    store_dir = project_root / "data" / "vector_store" / "index"

    kb = KnowledgeBase(store_dir)
    rag = RAGQA()

    print("\n📚 Academic RAG System (type 'exit' to quit)\n")

    while True:
        question = input("❓ Question: ").strip()
        if question.lower() == "exit":
            break

        results = kb.search(question, top_k=3)

        print("\n🔍 Top relevant chunks:\n")
        for i, res in enumerate(results):
            print(f"[{i+1}] Score: {res['score']:.4f}")
            print(f"Section: {res['metadata'].get('section')}")
            print(res["content"][:300])
            print("-" * 80)

        contexts = [res["content"] for res in results]

        answer = rag.generate_answer(question, contexts)

        print("\n🧠 Answer:\n")
        print(answer)
        print("\n" + "=" * 100 + "\n")


if __name__ == "__main__":
    main()