import ast
import re
import sys


def parse_module(module_name):
    """
    Opens the module file, gets all the module objects.
    """
    with open(module_name, "r") as module:
        return ast.parse(module.read(), filename=module_name)


def syntax_checking(module):
    """
    Checks the correct name of functions, classes, and methods of the class.

    regex_func_or_class - regular expression for checking
                          the name of a separate function or class.
    regex_methods_class - regular expression
                          for checking class method names.
    regex_service_methods_class - regular expression
                                  for excluding service methods __init__, etc.

    Verification procedure:
    1. All functions in the module are checked.
    2. All classes in the module are checked.
    3. The methods of the class are checked.

    """
    regex_func_or_class = "^[A-Z]{1}[a-z]{2}[a-zA-Z]+"
    regex_methods_class = "^[a-z]{1}[a-z_]+[a-z]+$"
    regex_service_methods_class = "^[_]{2,2}[a-zA-Z]+[_]{2,2}$"
    for obj in module.body:
        if (isinstance(obj, ast.FunctionDef) and
            not re.match(regex_func_or_class,
                         obj.name)):
            return 0
        if isinstance(obj, ast.ClassDef):
            if not re.match(regex_func_or_class, obj.name):
                return 0
            for method in obj.body:
                if (not re.match(regex_methods_class, method.name) and
                   not re.match(regex_service_methods_class, method.name)):
                    return 0
    return 1


def start_script(module_name):
    """
    Running the script.
    """
    module = parse_module(module_name)
    return syntax_checking(module)


if __name__ == "__main__":
    try:
        for module_name in sys.argv[1:]:
            print(start_script(module_name))
    except Exception:
        raise Exception("Error, pass the data in the format: "
                        "python syntax_check.py <file path>")
