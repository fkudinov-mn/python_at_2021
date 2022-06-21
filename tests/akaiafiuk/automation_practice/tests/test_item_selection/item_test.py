from python_at_2021.tests.akaiafiuk.automation_practice.pages.main_page import MainPage


def test_items(session):
    """Verify that there is more than one item on the Main page"""
    items = MainPage(session).open().items
    assert len(items) > 1


def test_item_name(session):
    """Verify that Item Name on the Main page matches with the item name on Item page"""
    main_page = MainPage(session)
    item_name_main_page = main_page.open().items[0].text
    item_name_item_page = main_page.items[0].open_item().name
    assert item_name_main_page == item_name_item_page


def test_item_description(session):
    """Verify that Item Description is present on the Item page"""
    main_page = MainPage(session)
    item_description = main_page.open().items[0].open_item().description
    assert len(item_description) > 0
