
from mock_data import mock_simple_data, mock_complex_data, mock_broken_url
from verification import HyperlinkVerifier
from pathlib import Path
import nltk

curr_dir = Path(__file__).parent
nltk_data_path = curr_dir / '../models/nltk_data'
if (nltk_data_path not in nltk.data.path):
    nltk.data.path.append(nltk_data_path)

verifier = HyperlinkVerifier()
for data in mock_simple_data:
    validation_code = verifier.read_url(data['hyperlink'])
    if (validation_code > 2):
        raise Exception('invalid url')
    result = verifier.validate(data['passage_context'])
    print(result)

# for data in mock_broken_url:
#     validation_code = verifier.read_url(data['hyperlink'])
#     if (validation_code > 2):
#         raise Exception('invalid url')
#     result = verifier.validate(data['passage_context'])
#     print(result)
