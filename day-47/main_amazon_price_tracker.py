from amazon_website_scrapping import Amazon_Site_Products

product = Amazon_Site_Products()

price_of_product = product.get_prices()
product.send_updates(price_of_product)