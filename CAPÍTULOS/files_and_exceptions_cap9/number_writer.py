from pathlib import Path
import json

numbers = [2, 3, 5, 7, 11, 13]

path = Path('CAPÍTULOS/files_and_exceptions_cap9/numbers.json')

contents = json.dumps(numbers)
path.write_text(contents)