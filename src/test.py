
from mock_data import mock_simple_data, mock_complex_data, mock_broken_url
from verification import HyperlinkVerifier

verifier = HyperlinkVerifier()
# for data in mock_simple_data:
#     validation_code = verifier.read_url(data['hyperlink'])
#     if (validation_code > 2):
#         raise Exception('invalid url')
#     result = verifier.validate(data['passage_context'])
#     print(result)

for data in mock_broken_url:
    validation_code = verifier.read_url(data['hyperlink'])
    if (validation_code > 2):
        raise Exception('invalid url')
    result = verifier.validate(data['passage_context'])
    print(result)
