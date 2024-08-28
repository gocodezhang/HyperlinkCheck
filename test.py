
from mock_data import mock_simple_data, mock_complex_data, mock_broken_url
from src.verification import HyperlinkVerifier
from src.nlp import classifier
from pathlib import Path
from dotenv import load_dotenv
import nltk
import logging

logging.basicConfig(level=logging.INFO)
load_dotenv()
curr_dir = Path(__file__).parent
nltk_data_path = curr_dir / './models/nltk_data'
if (nltk_data_path not in nltk.data.path):
    nltk.data.path.append(nltk_data_path)

verifier = HyperlinkVerifier()
for data in mock_simple_data:
    validation_code = verifier.read_url(data['hyperlink'])
    print(validation_code)
    if (validation_code > 0):
        raise Exception('invalid url')
    result = verifier.validate(data['passage_context'])
    print(result)

# print(classifier("Hi, I recently bought a device from your company but it is not working as advertised and I would like to get reimbursed!", [
#       "refund", "legal", "faq"]))
