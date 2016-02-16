import re

UNDERSCORIZE_SPECIAL_CASES = dict(
    RhostsRSAAuthentication='rhosts_rsa_authentication',
)


def underscorize(value):
    """Converts a CamelCaseName to camel_case_name

    Cases like RequestTTY will only insert an underscore for the first
    uppercase character. Uses :var:`UNDERSCORIZE_SPECIAL_CASES` to map
    certain special cases.

    Args:
        value (str): The string to underscorize

    Returns:
        str: The newly minted underscorized version
    """
    def replace(match):
        return '{0}{1}'.format(
                '_' if match.start() > 0 else '',
                match.group(1).lower()
        )

    special_case = UNDERSCORIZE_SPECIAL_CASES.get(value)
    if special_case:
        return special_case
    else:
        return re.sub(r'([A-Z]+)', replace, value)



class ManFile(object):
    CONTROL_CODE_REGEX = re.compile('((.)\x08\\2)')
    ARGUMENT_REGEX = re.compile("``(\w+)''")

    def __init__(self, file):
        self.file = file
        self.options = {}

        self.parse()

    def parse(self):
        with open(self.file, 'r') as f:
            current_option = False
            past_host = False  # Between description and pattern lies our option
            for line in f:
                if not line or not line.strip():
                    continue

                line_had_control_codes = True if '\x08' in line else False
                line = self._remove_control_codes(line)
                if not past_host:
                    if line.startswith('{0:<5}Host'.format('')):
                        past_host = True
                    continue
                elif line.strip() == 'PATTERNS':
                    break

                if line.startswith('{0:<13}'.format('')) and current_option:
                    self._extract_description_and_arguments(current_option,
                                                            line)
                elif re.match(r' {5}\w', line) and line_had_control_codes:
                    line = line.split()
                    current_option = line[0]
                    self.options[current_option] = {
                        'valid_arguments': set(),
                        'description': [],
                    }
                    if len(line) > 1:
                        self._extract_description_and_arguments(
                            current_option,
                            line[1]
                        )

    def _extract_description_and_arguments(self, current_option, line):
        self.options[current_option]['description'].append(line.strip())
        self.options[current_option]['valid_arguments'].update(
            self._extract_valid_arguments(line.strip())
        )

    def _remove_control_codes(self, line):
        return self.CONTROL_CODE_REGEX.sub(r'\2', line)

    def _extract_valid_arguments(self, line):
        return self.ARGUMENT_REGEX.findall(line)

    def valid_arguments(self, option):
        """Returns the valid arguments parsed for an option

        Args:
            option (str): The name of a parsed option

        Raises:
            KeyError: When the option doesn't exist

        Returns:
            set: All the parsed valid sets for this option
        """
        return self.options[option]['valid_arguments']

    def description(self, option):
        """Returns the description of an option

        Args:
            option (str): The name of a parsed option

        Raises:
            KeyError: When the option doesn't exist

        Returns:
            str: The string describing the option
        """
        return '\n'.join(
            map(lambda s: s.strip(), self.options[option]['description']))

    def format_option_dict(self, option):
        """Returns a dict in Ansible's `argument_spec`_ format for  the option

        Args:
            option (str): The name of a parsed option

        Raises:
            KeyError: When the option doesn't exist

        Returns:
            dict: `argument_spec`_ formatted dict for the option, ready to
                  be pasted into the library

        .. _argument_spec: http://docs.ansible.com/ansible/developing_modules.html#common-module-boilerplate
        """  # noqa
        arguments = self.valid_arguments(option)
        if len(arguments) > 2:
            return dict(default=None, choices=list(arguments))
        elif arguments == {'yes', 'no'}:
            return dict(default=None, type='bool')
        # Don't know any option that would use this, so warn when it's seen
        elif len(arguments) == 1 and not arguments == {'none'}:
            raise ValueError(
                "Don't know what to do with argument value '{0}' "
                "for option '{1}".format(
                    arguments,
                    option
                )
            )
        else:
            return dict(default=None, type='str')
