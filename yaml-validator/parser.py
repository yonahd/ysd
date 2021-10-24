import yaml
import logging


class Parser:
    __yaml_file = None

    def __init__(self, yaml_file):
        self.__yaml_file = yaml_file

    def yaml_to_dict(self):
        with open(self.__yaml_file, "r") as current_file:
            try:
                return yaml.safe_load(current_file)
            except yaml.YAMLError as exc:
                logging.error(exc)
