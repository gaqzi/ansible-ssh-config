import pytest

from extract_options import ManFile


class TestManSimpleExtraction(object):
    man_file = None

    def setup_method(self, method):
        self.man_file = ManFile('man/one-option')

    def test_extract_names(self):
        assert self.man_file.options.keys() == ['RequestTTY']

    def test_extracts_valid_values(self):
        assert (
            self.man_file.options['RequestTTY']['valid_arguments'] == {'yes', 'no', 'force', 'auto'}
        )


class TestManFullExtraction(object):
    man_file = None

    def setup_method(self, method):
        self.man_file = ManFile('man/full')

    def test_assert_found_all_options(self):
        assert len(self.man_file.options.keys()) == 77

    def test_assert_found_valid_arguments(self):
        pass
