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
        request_tty = self.man_file.valid_arguments('RequestTTY')
        assert request_tty == {'yes', 'no', 'force', 'auto'}

        clear_all_fwding = self.man_file.valid_arguments('ClearAllForwardings')
        assert clear_all_fwding == {'yes', 'no'}

        control_master = self.man_file.valid_arguments('ControlMaster')
        assert control_master == {'ask', 'auto', 'yes', 'no', 'autoask'}

    def test_description(self):
        assert self.man_file.description('RequestTTY') == '\n'.join([
            "Specifies whether to request a pseudo-tty for the session.  The",
            "argument may be one of: ``no'' (never request a TTY), ``yes''",
            "(always request a TTY when standard input is a TTY), ``force''",
            "(always request a TTY) or ``auto'' (request a TTY when opening a",
            "login session).  This option mirrors the -t and -T flags for",
            "ssh(1).",
        ])


class TestManFormatOptionDict(object):
    man_file = None

    def setup_method(self, method):
        self.man_file = ManFile('man/full')

    def test_with_multiple_choices(self):
        assert self.man_file.format_option_dict('RequestTTY') == dict(
            default=None, choices=['auto', 'yes', 'force', 'no'],
        )

    def test_with_boolean(self):
        assert self.man_file.format_option_dict('IdentitiesOnly') == dict(
            default=None, type='bool'
        )

    def test_with_free_text_that_has_none_to_disable(self):
        # ProxyCommand can optionally be force-set to 'none', while it also takes
        # a string which is a command to execute. It wouldn't work to treat this specially,
        # so just ignore that there is an argument if the argument is 'none'.
        assert self.man_file.format_option_dict('ProxyCommand') == dict(
            default=None, type='str'
        )

    def test_with_free_text(self):
        assert self.man_file.format_option_dict('XAuthLocation') == dict(
            default=None, type='str'
        )
