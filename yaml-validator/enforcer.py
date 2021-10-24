from parser import Parser
from common import Rules
from logger import ColorLog


class Enforce:
    __values_parser = None
    __rules_parser = None
    __rules = None
    __values = None
    __all_rules = None
    __logger = None
    __rule_checker = None

    def __init__(self, required_files: dict):
        self.__rules_parser = Parser(required_files['rules'])
        self.__values_parser = Parser(required_files['values'])
        self.__values = self.__values_parser.yaml_to_dict()
        self.__rules = self.__rules_parser.yaml_to_dict()
        self.__all_rules = self.__rules['required'] | self.__rules['optional']
        self.__logger = ColorLog()
        self.__rule_checker = Rules()

    def __eval_rule(self, value, rules, full_field_name):
        if self.__rule_checker.field_exist(rules, value) is True:
            self.__logger.print_success_type(full_field_name)
        else:
            self.__logger.print_fail_rule(full_field_name)

    def __check_field(self, value, value_type, values, rules, full_field_name):
        if type(value_type) is dict:
            if self.__rule_checker.field_exist(rules, value) and type(rules[value]) is dict:
                for value_r, value_type_r in value_type.items():
                    self.__check_field(value_r, value_type_r, values[value], rules[value],
                                       full_field_name + '.' + value_r)
            else:
                self.__logger.print_fail_rule_sub(full_field_name)
        else:
            self.__eval_rule(value, rules, full_field_name)

    def check_fields(self):
        print("\n---Checking fields exist---")
        for value, value_type in self.__values.items():
            self.__check_field(value, value_type, self.__values, self.__all_rules, value)
