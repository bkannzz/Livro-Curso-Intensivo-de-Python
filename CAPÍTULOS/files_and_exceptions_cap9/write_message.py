from pathlib import Path

contents = 'I love programming'
contents += 'I love creating new games.\n'
contents += 'I also love working with data.\n'

path = Path('CAPÍTULOS/files_and_exceptions_cap9/programming.txt')
path.write_text(contents) # escreve em um arquivo 