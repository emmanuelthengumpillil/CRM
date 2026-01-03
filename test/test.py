import pytest
import storage

f  = 'crm.csv'

def test_read_csv():
    assert storage.read_csv(f)["success"] == True

def test_header_is_OK():
    assert storage.read_csv(f)["success"] == True

