from bs4 import BeautifulSoup
import requests as r
import random

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

def monte_carlo(days):
    """ Runs a Monte Carlo simulation to predict average yearly revenue."""
    menu_items, prices = starbucks_menu()
    avg_customers = random.randint(600,700)# Average number of customers in the store per day.

    # Average revenue from a customer order.
    yearly_revenue = 0
    for i in range(days):
        daily_revenue = 0 # Resets daily revenue at start of day.
        for j in range(avg_customers):
            revenue_per_customer = 0 # Resets revenue per customer for new customer.
            num_items_ordered = random.choice([1,2,3]) # Number of items customer orders.
            for k in range(num_items_ordered):
                prices_of_items_ordered = random.choice(prices) # Picks random items ordered by customer.
                revenue_per_customer += prices_of_items_ordered
                #print(f"Customer {j} ordered {num_items_ordered} things worth ${revenue_per_customer}")
            daily_revenue += revenue_per_customer
        #print(f"Revenue for Day #{i}: ${daily_revenue}")
        yearly_revenue += daily_revenue
    print(f"Yearly revenue is: ${yearly_revenue}")
monte_carlo(365)
