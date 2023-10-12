import os
from requests.utils import requote_uri

markdown = '''
# Data Structures & Algorithms

All the data structures and algorithms I have implemented in C++ & Python.

## Table of Contents
'''
for dir in os.listdir('./'):
    if not os.path.isdir(dir) or dir.startswith('.'):
        continue
    
    markdown += f'## {dir}\n'
    print(dir)
    for subdir, dirs, files in os.walk(f'./{dir}'):
        if subdir.split("/")[-1] != dir:
            markdown += f'- {subdir.split("/")[-1]}\n'
        for file in files:
            if file.endswith('.cpp') or file.endswith('.py') or file.endswith('.c'):
                url = requote_uri(os.path.join(subdir, file))
                markdown += f'  - [{file}]({url})\n'
        # print()
        # markdown += '\n\n'
    
with open('README.md', 'w') as f:
    f.write(markdown)