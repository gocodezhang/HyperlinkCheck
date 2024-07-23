
from mock_data import mock_simple_data, mock_complex_data
from verification import HyperlinkVerifier

verifier = HyperlinkVerifier()
for data in mock_simple_data:
  verifier.read_url(data['hyperlink'])
  result = verifier.validate(data['passage_context'])
  print(result)




