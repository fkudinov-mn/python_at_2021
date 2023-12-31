import pytest
import requests
from python_at_2021.tests.akaiafiuk.book_store_ui.pages.books_page import BooksPage


@pytest.mark.books
def test_locators(session):
    """
    Verify that locators are correct and it is possible to test a separate table row
    """
    books_page = BooksPage(session).open()
    row = books_page.get_books_table().get_rows()[0]
    assert row.title == 'Git Pocket Guide'
    assert 'Richard E.' in row.author


@pytest.mark.books
def test_search(session):
    """
    Test search using exact match
    """
    books_page = BooksPage(session).open()
    row = books_page.open().get_books_table().get_rows()[0]
    title = row.title
    books_page.do_search(title)
    assert len(books_page.get_books_table().get_rows()) == 1


@pytest.mark.books
def test_column_names(session):
    """
    Test that column names are correct
    """
    expected_titles = ('Image', 'Title', 'Author', 'Publisher')
    books_page = BooksPage(session)
    columns = books_page.open().get_books_table().get_columns()
    assert len(columns) == len(expected_titles)
    assert all(text.text in expected_titles for text in columns)


@pytest.mark.books
def test_books_images(session):
    """
    Test that a valid image is displayed for each book
    """
    rows = BooksPage(session).open().get_books_table().get_rows()
    for row in rows:
        link = row.image.get_attribute('src')
        r = requests.head(link)
        assert r.headers['Content-Type'] == 'image/jpeg'


@pytest.mark.books
def test_books_links(session):
    """
    Test that bok links are not broken
    """
    rows = BooksPage(session).open().get_books_table().get_rows()
    for row in rows:
        link = row.link.get_attribute('href')
        r = requests.head(link)
        assert 200 <= r.status_code < 400
        r.raise_for_status()
