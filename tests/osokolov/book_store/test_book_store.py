
from tests.osokolov.book_store.book_store_page import BookStorePage


def test_book_store(browser):
    book_store = BookStorePage(browser)
    book_store.open()
    rows = book_store.get_book_rows()
    rows[0].get_title()
    book_store.verify_log_out_button()
    login_page = book_store.click_login_button()
    login_page.verify_login_page()
