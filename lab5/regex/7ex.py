def snake_camel(snake):
    words = snake.split('_')
    camel = words[0] + ''.join(word.capitalize() for word in words[1:])
    return camel

snake_str = "snake_case_example_string"
camel_str = snake_camel(snake_str)
print("Original string:", snake_str)
print("Converted string:", camel_str)