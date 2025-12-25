from pathlib import Path
from typing import List, Dict

from pptx import Presentation


def extract_slides(pptx_path: Path) -> List[Dict]:
    """
    Extract text slide-by-slide with slide-feature-aware chunking.
    Each slide becomes one chunk, but internal structure is respected.
    """
    presentation = Presentation(str(pptx_path))

    chunks = []

    for slide_idx, slide in enumerate(presentation.slides):
        slide_text_chunks = []  # will store text per feature

        for shape in slide.shapes:
            if hasattr(shape, "text"):
                text = shape.text.strip()
                if not text:
                    continue

                # Simple feature-based splitting
                if text.isupper():
                    # Consider uppercase text as a heading
                    slide_text_chunks.append(f"Heading: {text}")
                elif "\n" in text:
                    # Split bullet points into separate lines
                    bullets = [f"Bullet: {line.strip()}" for line in text.split("\n") if line.strip()]
                    slide_text_chunks.extend(bullets)
                else:
                    slide_text_chunks.append(text)

        if not slide_text_chunks:
            continue

        content = "\n".join(slide_text_chunks)

        chunks.append({
            "content": content,
            "metadata": {
                "source": pptx_path.name,
                "slide_number": slide_idx + 1,
                "document_type": "slides"
            }
        })

    return chunks chunks


