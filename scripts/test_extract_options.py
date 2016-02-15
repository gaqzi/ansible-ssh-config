from extract_options import ManFile


class TestManFullExtraction(object):
    man_file = None

    def setup_method(self, method):
        self.man_file = ManFile('man/full')

    def test_extract_names(self):
        assert 'RequestTTY' in self.man_file.options.keys()

    def test_assert_found_all_options(self):
        assert len(self.man_file.options.keys()) == 77

    def test_assert_found_valid_arguments(self):
        assert self.man_file.valid_arguments('RequestTTY') == {'yes', 'no', 'force', 'auto'}
        assert self.man_file.valid_arguments('ClearAllForwardings') == {'yes', 'no'}
        assert self.man_file.valid_arguments('ControlMaster') == {'ask', 'auto', 'yes', 'no', 'autoask'}

    def test_description(self):
        assert self.man_file.description('RequestTTY') == '\n'.join([
            "Specifies whether to request a pseudo-tty for the session.  The",
            "argument may be one of: ``no'' (never request a TTY), ``yes''",
            "(always request a TTY when standard input is a TTY), ``force''",
            "(always request a TTY) or ``auto'' (request a TTY when opening a",
            "login session).  This option mirrors the -t and -T flags for",
            "ssh(1).",
        ])
    man_file = None

    def setup_method(self, method):
        self.man_file = ManFile('man/full')

    def test_assert_found_all_options(self):
        assert len(self.man_file.options.keys()) == 77

    def test_assert_found_valid_arguments(self):
        pass
