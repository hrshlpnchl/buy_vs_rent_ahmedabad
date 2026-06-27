from rapidfuzz import process, fuzz
from config import SHELA_SOCIETIES

def resolve(raw_name: str) -> str | None:
    if not raw_name: return None
    match, score, _ = process.extractOne(
        raw_name, SHELA_SOCIETIES, scorer=fuzz.token_set_ratio
    )
    return match if score >= 80 else None   # tune threshold
