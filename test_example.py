from hellow import add
import pytest
  
def test_add():  
    assert add(1,2) == 3  
    assert add(2,2) == 4