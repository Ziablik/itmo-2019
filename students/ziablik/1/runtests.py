import os
import re
import subprocess

for directory in os.walk(".", topdown=False):
    if '.idea' not in directory[0] and directory[2]:
        for file in directory[2]:
            if re.match('test_\w*.py', file) is not None:
                process = subprocess.Popen(['python', directory[0] + '\\' + file])
                print(directory[0] + '\\' + file, end=' ... ', flush=True)
                process.wait()