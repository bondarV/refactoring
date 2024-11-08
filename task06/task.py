class NameLengthError(ValueError):
    def __init__(self, name, message="Ім'я повинно бути не менше 10 символів"):
        self.name = name
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.name} -> {self.message}'

def check_name_length(name):
    if name.isdigit():
        raise NameLengthError(name, "Ім'я не повинно бути числом")
    if len(name) < 10:
        raise NameLengthError(name)
    else:
        print(f"Ім'я '{name}' відповідає вимогам.")

if __name__ == '__main__':
    try:
        check_name_length("Ivan")
    except NameLengthError as e:
        print(e)

    try:
        check_name_length("12345")
    except NameLengthError as e:
        print(e)

    try:
        check_name_length("Oleksandr")
    except NameLengthError as e:
        print(e)
