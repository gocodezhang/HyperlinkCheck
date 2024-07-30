from pathlib import Path
from transformers import pipeline

curr_dir = Path(__file__).parent
token_classification = pipeline(
    "token-classification", model=curr_dir / '../../models/keyphrase-extraction-kbir-inspec')


def keywords_extractor(str):
    # apply token classification to identify key words
    raw_output = token_classification(str)
    length = len(raw_output)

    # convert the model output into actual key words
    tags = {'words': [], 'scores': []}
    visited = set()
    index = 0
    while (index < length):
        curr_output = raw_output[index]
        # skip curr index if it is not B-KEY
        if (curr_output['entity'] != 'B-KEY'):
            index += 1
            continue

        # locate start/end for curr keyword
        start = curr_output['start']
        end = curr_output['end']
        score = curr_output['score'] * (end - start)
        # move until we find the next B-KEY
        while (index + 1 < length and raw_output[index + 1]['entity'] != 'B-KEY'):
            next_output = raw_output[index + 1]
            end = next_output['end']
            score += next_output['score'] * (end - next_output['start'])
            index += 1

        word = str[start: end]
        if (word not in visited):
            visited.add(word)
            tags['words'].append(word)
            tags['scores'].append(score / (end - start))

        index += 1

    return tags
