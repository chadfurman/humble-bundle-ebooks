import re
# from https://stackoverflow.com/questions/1175208/elegant-python-function-to-convert-camelcase-to-snake-case
def to_snake_case(str):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', str).lower()