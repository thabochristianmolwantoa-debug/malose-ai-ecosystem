import re

def clean_sepedi_text(text: str):
    # Specialized logic for Malose AI NSO priority
    text = text.replace("s^", "š").replace("S^", "Š")
    return re.sub(r'\bKea\b', 'Ke a', text).strip()