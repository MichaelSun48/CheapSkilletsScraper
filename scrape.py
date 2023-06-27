import requests
from bs4 import BeautifulSoup
import urllib



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


BASE_URL = "https://www.homegoods.com{}"
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}

r = requests.get('https://www.homegoods.com/us/store/browse/json/revealBrand.jsp?productId=7000029797', headers=HEADERS)
print(r.json())


kitchen_url = BASE_URL.format("/us/store/shop/kitchen-dining-cookware/_/N-919477670?ln=3:1#/us/store/products/kitchen-dining-cookware/_/N-919477670?No=0&Nr=AND%28isEarlyAccess%3Afalse%2Cproduct.siteId%3Ahomegoods%2COR%28product.catalogId%3Atjmaxx%29%29&&tag=va&va=true")


name_brands = ["ALL-CLAD", "LODGE", "CUISINART", "CALPHALON PREMIER", "OXO", "LE CREUSET"]


# page = requests.get(kitchen_url, headers=headers, timeout=5, allow_redirects = True )
# html_soup = BeautifulSoup(page.text, "html.parser")

# products = html_soup.find_all("div", class_=["product", "processed"])

# for data in products:
#     price = data.find("span", class_="product-price")
#     print(price.text.strip())

#     brand = data.find("span", class_="product-brand").text.strip()

#     if brand == "Reveal Brand":
#         product_href = data.find("a", "product-link")["href"]
#         product_url = BASE_URL.format(product_href)

#         product_page = requests.get(product_url, headers=headers, timeout=5, allow_redirects = True)
#         product_page_html = BeautifulSoup(product_page.text, "html.parser")

#         brand = product_page_html.find("h1", class_="product-brand").text
#     print(brand)

def extract_product_info(product_url):
    product_page = requests.get(product_url, headers=HEADERS, timeout=5, allow_redirects = True)
    product_page_html = BeautifulSoup(product_page.text, "html.parser")

    brand = product_page_html.find("h1", class_="product-brand").text.strip().upper()
    name = product_page_html.find("h2", class_="product-title").text.strip().upper()

    def extract_price_info(price):
        if "NEW PRICE" in price:
            return price.split()[-1]
        else:
            return price
    final_price = extract_price_info(product_page_html.find("span", class_="product-price").text.strip().upper())

    og_price = product_page_html.find("span", class_="price-comparison").text.strip().upper().split()[-2]
    print(og_price)



# extract_product_info("https://www.homegoods.com/us/store/jump/product/kitchen-dining-cookware/Made-In-Usa-12in-Hard-Anodized-Skillet-With-Trivet-Slightly-Blemished/7000025300?colorId=NS9861091&pos=1:12&N=919477670")