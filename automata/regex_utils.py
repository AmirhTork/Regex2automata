import string

def validate_regex(regex: str):
    allowed_chars = set(string.ascii_letters + string.digits + '|*+()')
    if not set(regex).issubset(allowed_chars):
        raise ValueError("Invalid characters in regex. Allowed: letters, digits, |, *, +, (, )")


def insert_concat(regex: str) -> str:
    """Insert explicit concatenation operator '.' where needed."""
    result = []
    for i in range(len(regex)):
        result.append(regex[i])
        if i + 1 < len(regex):
            if regex[i] not in '(|' and regex[i + 1] not in '|)*+':
                result.append('.')
    return ''.join(result)


def regex_to_postfix(regex: str) -> str:
    precedence = {'*': 4, '+': 4, '.': 3, '|': 2}
    output = []
    operator_stack = []
    regex = insert_concat(regex)

    for token in regex:
        if token in string.ascii_letters or token.isdigit():
            output.append(token)
        elif token == '(':
            operator_stack.append(token)
        elif token == ')':
            while operator_stack and operator_stack[-1] != '(':
                output.append(operator_stack.pop())
            operator_stack.pop()
        else:
            while (operator_stack and operator_stack[-1] != '(' and
                   precedence.get(operator_stack[-1], 0) >= precedence[token]):
                output.append(operator_stack.pop())
            operator_stack.append(token)

    while operator_stack:
        output.append(operator_stack.pop())

    return ''.join(output)
