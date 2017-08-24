from app.list_schools import *

def test_parse_html():
    with open("mocks/schools_tbody.html", "r") as html_file:
        document = html_file.read()
        schools = parse_html(document)
        assert(len(schools)) == 204 # ok to update this number as new data comes in (desired).

def test_parse_name():
    name_transformations = [
        {"dirty":"AKRON (1961)", "clean":"AKRON", "year":1961},
        {"dirty":"ARIZONA SUMMIT(formerly Phoenix - 2007)", "clean":"ARIZONA SUMMIT", "year":2007},
        {"dirty":"CALIFORNIA - Berkeley (1923)", "clean":"CALIFORNIA - BERKELEY", "year":1923},
        {"dirty":"CONCORDIA (2015)*", "clean":"CONCORDIA", "year":2015},
        {"dirty":"LA VERNE (2006-2011; 2012)", "clean":"LA VERNE", "year":2012},
        {"dirty":"MITCHELL|HAMLINE (2015)", "clean":"MITCHELL|HAMLINE", "year":2015}, # consider 'MITCHELL - HAMLINE'
        {"dirty":"NEVADA (2000) ", "clean":"NEVADA", "year":2000},
        {"dirty":"NEW ENGLAND LAW | BOSTON (1969)", "clean":"NEW ENGLAND LAW | BOSTON", "year":1969}, # consider 'NEW ENGLAND LAW - BOSTON'
        {"dirty":"PENNSYLVANIA STATE-Penn State Law (1931)", "clean":"PENNSYLVANIA STATE-PENN STATE LAW", "year":1931}, # consider "PENNSYLVANIA STATE - PENN STATE LAW"
        {"dirty":"ST. THOMAS (Florida) (1988)", "clean":"ST. THOMAS (FLORIDA)", "year":1988},
        {"dirty":"UNT Dallas (2017)", "clean":"UNT DALLAS", "year":2017}
    ]
    for transformation in name_transformations:
        name, year = parse_link_text(transformation["dirty"])
        assert name == transformation["clean"]
        assert year == transformation["year"]
