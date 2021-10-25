from termcolor import colored


class ColorLog:

    @staticmethod
    def print_fail_type(field: str, var_type: str) -> None:
        print(colored("FAILED: Field {} exists but is not type {}".format(field, var_type), 'red'))

    @staticmethod
    def print_fail_field(field: str) -> None:
        print(colored("FAILED: Field {} does not exist".format(field), 'red'))

    @staticmethod
    def print_fail_rule(field: str) -> None:
        print(colored("FAILED: Rule for field {} doesn't exist".format(field), 'red'))

    @staticmethod
    def print_fail_rule_sub(field: str) -> None:
        print(colored("FAILED: Rule for field {} doesn't exist".format(field), 'red'))

    @staticmethod
    def print_field_optional(field: str) -> None:
        print(colored("Field {} does not exist -- optional".format(field), 'blue'))

    @staticmethod
    def print_success_type(field: str) -> None:
        print(colored("SUCCESS: Field {} exists and is correct type".format(field), 'green'))

    @staticmethod
    def print_success_field(field: str) -> None:
        print(colored("SUCCESS: Rule for field {} exist".format(field), 'green'))
