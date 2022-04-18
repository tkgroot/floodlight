import pytest
import h5py
import urllib.request
from floodlight.io.eigd import load_eigd, _download, _unpack


@pytest.mark.unit
def test_load_eigd() -> None:
    assert load_eigd() == ["No", "Yes"]


@pytest.mark.unit
def test__download(monkeypatch):
    class MockResponse(object):
        def __init__(self):
            self.fp = 'Hello World'
            self.status = 200
            self.reason = "OK"
            self.url = 'https://test.com/file.zip'

        def read(self):
            return self.fp

    def mock_get(url):
        return MockResponse()

    monkeypatch.setattr(urllib.request, "urlopen", mock_get, raising=True)
    x, y = _download()
    assert (x, y) == (200, "Hello World")


@pytest.mark.unit
def test__unpack():
    res = _unpack()
    assert res is True
