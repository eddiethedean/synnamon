__version__ = '0.1.5'

import os
import pathlib
from os.path import exists
from zipfile import ZipFile


path = pathlib.Path(__file__).parent.resolve()
zip_path = os.path.join(path, 'data/en_thesaurus_dict.json.zip')
unzip_path = os.path.join(path, 'data/en_thesaurus_dict.json')
unzip_folder = os.path.join(path, 'data')

if not exists(unzip_path):
    with ZipFile(zip_path, 'r') as zObject:
        zObject.extractall(path=unzip_folder)

from synnamon.get_syns import get_syns