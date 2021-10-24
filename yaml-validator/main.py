import argparse
from evaluator import Eval
from enforcer import Enforce


def required_files():
    parser = argparse.ArgumentParser(description='Lint a values file')
    parser.add_argument('--values', '-v', type=str, required=True,
                        help='Yaml file to lint')
    parser.add_argument('--rules', '-r', required=True, type=str,
                        help='Rules to use in linting process')
    parser.add_argument('--enforce', '-e', required=False, action='store_true',
                        help='Enforce all args in Yaml exist in rules')
    return vars(parser.parse_args())


if __name__ == '__main__':
    files = required_files()
    evaluator = Eval(files)
    evaluator.check_rules()
    if files['enforce']:
        enforcer = Enforce(files)
        enforcer.check_fields()
