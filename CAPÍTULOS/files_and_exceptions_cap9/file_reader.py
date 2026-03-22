from pathlib import Path # localiza a localização exata de um arquivo

path = Path('CAPÍTULOS/files_and_exceptions_cap9/pi_digits.txt')
contents = path.read_text().rstrip()
print(contents)

lines = contents.splitlines() # mostra todas as linhas do arquivo
for line in lines:
    print(line)