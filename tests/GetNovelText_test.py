import sys, string
sys.path.insert(0,'./app/')

import pytest, gutenbergpy.textget, GetNovelText


@pytest.fixture
def sample_text():
    book = gutenbergpy.textget.get_text_by_id(890)
    return book

def test_get_book(sample_text):
    assert type(GetNovelText.get_book(890)) is bytes

def test_clean_book_type(sample_text):
    assert type(GetNovelText.clean_book(sample_text)) is list

def test_clean_book_word_length(sample_text):
    book = GetNovelText.clean_book(sample_text)
    valid = True
    for page in book:
        if len(page) < 4:
            valid = False
            break
    assert valid == True

def test_capitalizaton_clean_book(sample_text):
    book = GetNovelText.clean_book(sample_text)
    valid = True
    for page in book:
        if page[0] not in string.ascii_uppercase:
            valid = False
            break
    assert valid == True
    
