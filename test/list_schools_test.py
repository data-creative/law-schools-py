from app.list_schools import *

def test_clean_href():
    dirty_href = '\\"http://www.abarequireddisclosures.org/\\"'
    assert clean_href(dirty_href) == 'http://www.abarequireddisclosures.org/'

def test_clean_name():
    names = [
        {"dirty":"AKRON (1961)", "clean":"AKRON"},
        {"dirty":"ARIZONA SUMMIT(formerly Phoenix - 2007)", "clean":"ARIZONA SUMMIT"},
        {"dirty":"CALIFORNIA - Berkeley (1923)", "clean":"CALIFORNIA - BERKELEY"},
        {"dirty":"CONCORDIA (2015)*", "clean":"CONCORDIA"},
        {"dirty":"MITCHELL|HAMLINE (2015)", "clean":"MITCHELL|HAMLINE"}, # consider 'MITCHELL - HAMLINE'
        {"dirty":"NEVADA (2000) ", "clean":"NEVADA"},
        {"dirty":"NEW ENGLAND LAW | BOSTON (1969)", "clean":"NEW ENGLAND LAW | BOSTON"}, # consider 'NEW ENGLAND LAW - BOSTON'
        {"dirty":"PENNSYLVANIA STATE-Penn State Law (1931)", "clean":"PENNSYLVANIA STATE-PENN STATE LAW"}, # consider "PENNSYLVANIA STATE - PENN STATE LAW"
        {"dirty":"ST. THOMAS (Florida) (1988)", "clean":"ST. THOMAS (FLORIDA)"},
        {"dirty":"UNT Dallas (2017)", "clean":"UNT DALLAS"}
    ]

    for name in names:

        assert clean_name(name["dirty"]) == name["clean"]
