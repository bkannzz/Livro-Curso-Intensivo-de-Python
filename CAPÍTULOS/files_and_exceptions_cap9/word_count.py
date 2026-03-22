from pathlib import Path

def count_words(path):
    """Conta o número aproximado de palavras em um arquivo"""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print('Sorry, the file {} does not exist.'.format(path))
    else:
        words = contents.split()
        num_words = len(words)
        print('The file {} has about {} words.'.format(path, num_words))

filenames = ['CAPÍTULOS/files_and_exceptions_cap9/pi_digits.txt',
'CAPÍTULOS/files_and_exceptions_cap9/pi_digits']

for filename in filenames:
    path = Path(filename)
    count_words(path)