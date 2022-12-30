import pytest, gutenbergpy.textget, string, GetNovelText


@pytest.fixture
def sample_text():
    book = gutenbergpy.textget.get_text_by_id(890)
    return book

def test_get_book(sample_text):
    assert type(GetNovelText.get_book(890)) is bytes



