from g2p_en import G2p
from difflib import SequenceMatcher


def pronunciation_score(transcript, expected_transcript):
    #both transcripts will be translated phonemically.
    #the expected transcript should aready be broken down and formatted correctly in a json file.
    #for the scoring process each section of the breakdown will compared to each other and the code should keep track of how many chunks match
    #everytime a chunk does not match the score will decrease. 
    #if there is time; implement a way for the app to keep track of what chunks were incorrect and incorporate suggestions on how to improve in the feedback when working with gemini

    #maybe disregard this or keep for simplicity/testing
    #if (transcript != expected_pronunciation):
        #"Try again!"

    #scoring output will be expected_pronunciation, detected_pronunciation, matched_chunks, confidence (similar layout as prototype; but not visible to user after testing)

    detected_phonemes = G2p(transcript)
    expected_phonemes = G2p(expected_transcript)

    matched_phonemes = SequenceMatcher(None, detected_phonemes, expected_phonemes)
    score = matched_phonemes.ratio()

    return {
        "detected_pronunciation": detected_phonemes,
        "expected_pronunciation": expected_phonemes,
        "confidence": score
    }