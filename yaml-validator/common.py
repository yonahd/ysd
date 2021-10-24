
class Rules:

    @staticmethod
    def check_field_type(rule_value, rule_type: str) -> bool:
        if type(rule_value).__name__ == rule_type:
            return True
        return False

    @staticmethod
    def field_exist(yaml_dict: dict, field: str) -> bool:
        try:
            if yaml_dict[field]:
                return True
        except KeyError:
            return False


