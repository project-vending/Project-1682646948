
import os

folders = ['data', 'src', 'tests']
files = {
    'data': ['raw_data.csv', 'processed_data.csv'],
    'src': ['app.py'],
    'tests': ['test_app.py']
}

for folder in folders:
    os.makedirs(folder, exist_ok=True)
    for file in files[folder]:
        with open(os.path.join(folder, file), 'w') as f:
            pass
