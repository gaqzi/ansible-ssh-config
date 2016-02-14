import re


class ManFile(object):
    CONTROL_CODE_REGEX = re.compile('((.)\x08\\2)')
    ARGUMENT_REGEX = re.compile("``(\w+)''")

    def __init__(self, file):
        self.file = file
        self.options = {}

        self.options['RequestTTY'] = {
            'valid_arguments': {'yes', 'no', 'force', 'auto'},
            'description': """Specifies whether to request a pseudo-tty for the session.  The
             argument may be one of: ``no'' (never request a TTY), ``yes''
             (always request a TTY when standard input is a TTY), ``force''
             (always request a TTY) or ``auto'' (request a TTY when opening a
             login session).  This option mirrors the --tt and --TT flags for
             ssh(1).
            """
        }
        self.parse()

    def parse(self):
        with open(self.file, 'r') as f:
            current_option = False
            for line in f:
                if not line:
                    continue

                if line.startswith('{0:<13}'.format('')):
                    self.options[current_option]['description'].append(line.strip())
                    self.options[current_option]['valid_arguments'].update(self._extract_valid_arguments(line))
                elif line.startswith('{0:<5}'.format('')):
                    line = self._remove_control_codes(line.strip())
                    current_option = line
                    self.options[current_option] = {
                        'valid_arguments': set(),
                        'description': [],
                    }
                else:
                    print(line.strip())

    def _remove_control_codes(self, line):
        return self.CONTROL_CODE_REGEX.sub(r'\2', line)

    def _extract_valid_arguments(self, line):
        return self.ARGUMENT_REGEX.findall(line)
