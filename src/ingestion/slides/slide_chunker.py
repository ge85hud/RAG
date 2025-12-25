from pathlib import Path
from typing import List, Dict

from pptx import Presentation


def extract_slides(pptx_path: Path) -> List[Dict]:
    """
    Extract text slide-by-slide.
    Each slide becomes one chunk.
    """
    presentation = Presentation(str(pptx_path))

    chunks = []

    for slide_idx, slide in enumerate(presentation.slides):
        slide_text = []

        for shape in slide.shapes:
            if hasattr(shape, "text"):
                text = shape.text.strip()
                if text:
                    slide_text.append(text)

        if not slide_text:
            continue

        content = "\n".join(slide_text)

        chunks.append({
            "content": content,
            "metadata": {
                "source": pptx_path.name,
                "slide_number": slide_idx + 1,
                "document_type": "slides"
            }
        })

    return chunks

