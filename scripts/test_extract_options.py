import pytest

from extract_options import ManFile


@pytest.fixture
def man_file():
    return ManFile('man/one-option')


class TestManFile(object):
    def test_extract_names(self, man_file):
        assert man_file.options.keys() == ['RequestTTY']

    def test_extracts_valid_values(self, man_file):
        assert man_file.options['RequestTTY']['valid_arguments'] == {'yes', 'no', 'force', 'auto'}
