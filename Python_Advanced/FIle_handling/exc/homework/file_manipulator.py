import io
from io import open
from os import remove
def create_file(file_name):
    with open(f'.\\{file_name}', 'w'):
        pass
def add_to_file(file_name, text):
    with open(f'.\\{file_name}', 'a') as file:
        file.write(f'{text}\n')
def replace(file_name, old_str, new_str):
    try:
        with open(f'.\\{file_name}', 'r+') as file:
            file_content = file.read().replace(old_str, new_str)
            file.seek(0)
            file.truncate()
            file.write(file_content)
    except FileNotFoundError:
        print('An error occurred')

def delete(file_name):
    try:
        remove(f'.\\{file_name}')
    except FileNotFoundError:
        print('An error occurred')

while True:
    command = input()
    if command == 'End':
        break

    command_parts = command.split('-')
    the_command = command_parts[0]
    the_file = command_parts[1]
    if the_command == "Create":
        create_file(the_file)

    elif the_command == 'Add':
        text = command_parts[2]
        add_to_file(the_file, text)
    elif the_command == 'Replace':
        old_str, new_str = command_parts[2], command_parts[3]
        replace(the_file, old_str, new_str)

    elif the_command == 'Delete':
        delete(the_file)

