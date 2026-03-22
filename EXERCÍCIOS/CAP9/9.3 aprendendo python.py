#EX 9.3 Aprendendo Python

from pathlib import Path

path = Path('EXERCÍCIOS/CAP9/learning_python.txt')
contents = path.read_text()
print(contents)
codigo = []

for line in contents.splitlines():
    codigo.append(line)
    print(line)

print(codigo)

#EX 9.4 Aprendendo C

for line in contents.splitlines():
    linha_nova = line.replace('Python', 'Java')
    codigo.append(linha_nova)
    print(linha_nova)