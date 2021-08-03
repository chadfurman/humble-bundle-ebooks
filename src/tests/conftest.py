import sys

import pytest
import os

pytest_plugins = [
]

files = os.listdir('../fixtures')
for file in files:
    name = os.path.splitext(os.path.basename(file))[0]
    if file[0] != '_':
        pytest_plugins.append('fixtures.'+name)
