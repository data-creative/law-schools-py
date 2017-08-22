from app.list_schools import *

def test_clean_href():
    assert clean_href('\\"http://www.abarequireddisclosures.org/\\"') == 'http://www.abarequireddisclosures.org/'
