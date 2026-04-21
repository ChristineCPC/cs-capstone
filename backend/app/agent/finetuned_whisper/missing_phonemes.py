import difflib

def get_missing_phonemes(detected_phonemes, expected_phonemes):
    matched_phonemes = difflib.SequenceMatcher(None, detected_phonemes, expected_phonemes)

    missing_phonemes = []

    for tag, i1, i2, j1, j2 in matched_phonemes.get_opcodes():
        if tag == 'delete':
            # if the user missed a phoneme/sound
            missing_phonemes.append({"type": "skipped", "expected": expected_phonemes[j1:j2]})
        elif tag == 'replace':
            #if the user said a phoneme wrong
            missing_phonemes.append({"type": "incorrect", "expected": expected_phonemes[j1:j2], "got": detected_phonemes[i1:i2]})
        elif tag == 'insert':
            #if the user added an additional phoneme
            missing_phonemes.append({"type": "extra", "got": detected_phonemes[i1:i2]})

    return missing_phonemes