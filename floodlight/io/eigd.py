import shutil
import tempfile
import urllib.request
from typing import List

from settings import EIGD_HOST_URL, ROOT_DIR


def load_eigd() -> List:
    return ["No", "Yes"]


def _download():
    response = urllib.request.urlopen(EIGD_HOST_URL)
    return response.status, response.read()


def _unpack():
    status, file = _download()

    tmp = tempfile.NamedTemporaryFile()
    tmp.write(file)

    shutil.unpack_archive(tmp.name, f'{ROOT_DIR}/tmp', format='zip')
