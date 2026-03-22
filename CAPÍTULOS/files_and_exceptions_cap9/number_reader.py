from pathlib import Path
import json

path = Path('CAPÍTULOS/files_and_exceptions_cap9/numbers.json')

contents = path.read_text()
numbers = json.loads(contents)

print(numbers)