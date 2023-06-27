import requests
from bs4 import BeautifulSoup


# 0. What site do you want to search on (TODO)
# 1. What category do you want to search for (TODO)
# 2. What do you want to filter by (brand, key word) <-- Most important thing 
# 3. Do another search?

# Example Entry: 
#   Brand: All-Clad 
#   Name: 10 inch stainless steel pan 
#   Listed MSRP: $100
#   Price: $50
#   Link to buy: https://www.homegoods.com/.....


# TODOs:
# 1. Save data to local storage to avoid excessive requests 
#   1.1. Serialize python dictionary to json to maintain readability
# 2. Create filter by brand and keyword functions 
# 3. Create simple cli
# 4. profit 


base_url = "https://www.homegoods.com{}"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}

kitchen_url = base_url.format("/us/store/shop/kitchen-dining-cookware/_/N-919477670?ln=3:1#/us/store/products/kitchen-dining-cookware/_/N-919477670?No=0&Nr=AND%28isEarlyAccess%3Afalse%2Cproduct.siteId%3Ahomegoods%2COR%28product.catalogId%3Atjmaxx%29%29&&tag=va&va=true")


name_brands = ["ALL-CLAD", "LODGE", "CUISINART", "CALPHALON PREMIER", "OXO"]


page = requests.get(kitchen_url, headers=headers, timeout=5, allow_redirects = True )
html_soup = BeautifulSoup(page.text, "html.parser")

products = html_soup.find_all("div", class_=["product", "processed"])

for data in products:
    price = data.find("span", class_="product-price")
    print(price.text.strip())

    brand = data.find("span", class_="product-brand").text.strip()

    if brand == "Reveal Brand":
        product_href = data.find("a", "product-link")["href"]
        product_url = base_url.format(product_href)

        product_page = requests.get(product_url, headers=headers, timeout=5, allow_redirects = True)
        product_page_html = BeautifulSoup(product_page.text, "html.parser")

        brand = product_page_html.find("h1", class_="product-brand").text
    print(brand)
   