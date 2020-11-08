from bs4 import BeautifulSoup
import requests as r

def starbucks_menu():
    """ Scrapes menu items from starbucks (food, drinks, sizes, prices)."""
    menu_items = {}
    prices = []
    URL = 'https://www.fastfoodmenuprices.com/starbucks-prices/'
    page = r.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    table_results = soup.find_all(class_='row-hover')
    for items in table_results:
        for nested_items in items.tr.next_siblings:
            try:
                item_name = nested_items.td.string
                item_size = nested_items.td.next_sibling.next_sibling.string
                item_price = float(nested_items.td.next_sibling.next_sibling.next_sibling.next_sibling.input.attrs['value'].replace('$',''))
                prices.append(item_price)
                size_price = {item_size:item_price}
                if item_name in menu_items:
                    menu_items[item_name][item_size] = item_price
                else:
                    menu_items[item_name] = size_price
            except: # When None.
                pass
    return menu_items, prices
