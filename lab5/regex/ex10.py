def camel_to_snake(camel_case):
    snake_case = ''
    for x in camel_case:
        if x.isupper():
            snake_case += '_' + x.lower()
        else:
            snake_case += x

    if snake_case.startswith('_'):
        snake_case = snake_case[1:]
    return snake_case

camel_str = str(input())
snake_str = camel_to_snake(camel_str)
print("Original string:", camel_str)
print("Converted string:", snake_str)