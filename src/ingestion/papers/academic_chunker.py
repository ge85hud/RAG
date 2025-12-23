import re
from pathlib import Path
from typing import List, Dict

from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter


ACADEMIC_SECTION_PATTERNS = [
    r"\babstract\b",
    r"\bintroduction\b",
    r"\brelated work\b",
    r"\bbackground\b",
    r"\bmethodology\b",
    r"\bmethods\b",
    r"\bexperimental setup\b",
    r"\bexperiments\b",
    r"\bresults\b",
    r"\bdiscussion\b",
    r"\bconclusion\b",
    r"\bfuture work\b",
    r"\breferences\b",
]


def extract_pdf_text(pdf_path: Path) -> str:
    reader = PdfReader(str(pdf_path))
    pages = []

    for page in reader.pages:
        text = page.extract_text()
        if text:
            pages.append(text.strip())

    return "\n".join(pages)


def detect_sections(text: str) -> Dict[str, str]:
    """
    Split paper text into sections using academic heading heuristics.
    """
    section_regex = re.compile(
        r"\n(?=(" + "|".join(ACADEMIC_SECTION_PATTERNS) + r")\b)",
        flags=re.IGNORECASE
    )

    splits = section_regex.split(text)
    sections = {}
    current_section = "unknown"
    buffer = []

    for part in splits:
        part_lower = part.lower().strip()

        if any(re.fullmatch(pat.strip(r"\b"), part_lower)
               for pat in ACADEMIC_SECTION_PATTERNS):
            if buffer:
                sections[current_section] = "\n".join(buffer).strip()
                buffer = []
            current_section = part_lower
        else:
            buffer.append(part)

    if buffer:
        sections[current_section] = "\n".join(buffer).strip()

    return sections


def chunk_section(
    section_text: str,
    chunk_size: int = 800,
    chunk_overlap: int = 120
) -> List[str]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", " ", ""]
    )
    return splitter.split_text(section_text)


def chunk_academic_paper(
    pdf_path: Path
) -> List[Dict]:
    full_text = extract_pdf_text(pdf_path)
    sections = detect_sections(full_text)

    documents = []
    chunk_id = 0

    for section, text in sections.items():
        chunks = chunk_section(text)

        for chunk in chunks:
            documents.append({
                "content": chunk,
                "metadata": {
                    "source": pdf_path.name,
                    "section": section,
                    "chunk_id": chunk_id
                }
            })
            chunk_id += 1

    return documents