from parser import Parser
from common import Rules
from logger import ColorLog


class Eval:
    __values_parser = None
    __rules_parser = None
    __rules = None
    __values = None
    __required_rules = None
    __optional_rules = None
    __logger = None
    __rule_checker = None

    def __init__(self, required_files: dict):
        self.__rules_parser = Parser(required_files['rules'])
        self.__values_parser = Parser(required_files['values'])
        self.__values = self.__values_parser.yaml_to_dict()
        self.__rules = self.__rules_parser.yaml_to_dict()
        self.__required_rules = self.__rules['required']
        self.__optional_rules = self.__rules['optional']
        self.__logger = ColorLog()
        self.__rule_checker = Rules()

    def __eval_rule(self, rule, rule_type, values, required, full_field_name):
        if self.__rule_checker.field_exist(values, rule):
            if self.__rule_checker.check_field_type(values[rule], rule_type):
                self.__logger.print_success_type(full_field_name)
            else:
                self.__logger.print_fail_type(full_field_name, rule_type)
        elif required:
            self.__logger.print_fail_field(full_field_name)
        else:
            self.__logger.print_field_optional(full_field_name)

    def __check_rule(self, rule, rule_type, values, rules, full_field_name, required: bool):
        if type(rule_type) is dict:

            if self.__rule_checker.field_exist(values, rule):
                if self.__rule_checker.check_field_type(values[rule], "dict"):
                    for rule_r, rule_type_r in rule_type.items():
                        self.__check_rule(rule_r, rule_type_r, values[rule], rules[rule],
                                          full_field_name + '.' + rule_r, required)
                else:
                    self.__logger.print_fail_field(full_field_name)
            elif required:
                self.__logger.print_fail_field(full_field_name)
            else:
                self.__logger.print_field_optional(full_field_name)
        else:
            self.__eval_rule(rule, rule_type, values, required, full_field_name)

    def check_rules(self):
        print("---Checking required fields---")
        for rule, rule_type in self.__required_rules.items():
            self.__check_rule(rule, rule_type, self.__values, self.__required_rules, rule, required=True)
        print("---Checking optional fields---")
        for rule, rule_type in self.__optional_rules.items():
            self.__check_rule(rule, rule_type, self.__values, self.__required_rules, rule, required=False)