import re, json
from pathlib import Path

def convert_tags(text: str, ipa_map=None):
    def slow_handler(match):
        content = match.group(1).strip()
        if ipa_map:
            content = ipa_to_text(content)
        return f"{content}..."

    def emphasis_handler(match):
        content = match.group(1).strip()
        if ipa_map:
            content = ipa_to_text(content)
        return content.upper()

    text = re.sub(r"\[slow\](.*?)\[/slow\]", slow_handler, text)
    text = re.sub(r"\[emphasis\](.*?)\[/emphasis\]", emphasis_handler, text)

    print(text)

    return text


def ipa_to_text(ipa):
    current_dir = Path(__file__).parent
    phoneme_map_path = current_dir / "phoneme-map.json"

    with open(phoneme_map_path, "r") as file:
        data = json.load(file)

    ipa_map = data["IPA_TO_TEXT"]

    phonemes = sorted(ipa_map.keys(), key=len, reverse=True)

    result = ipa
    for p in phonemes:
        result = result.replace(p, ipa_map[p])

    return result