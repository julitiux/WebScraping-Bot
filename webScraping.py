from bs4 import BeautifulSoup
import requests
import time
import webbrowser

url = requests.get("https://www.mercadolibre.com.mx/sony-playstation-5-825gb-standard-color-blanco-y-negro/p/MLM16171888?pdp_filters=category:MLM167860#searchVariation=MLM16171888&position=1&type=product&tracking_id=14123963-f2bb-450f-969e-96b2756268ce")
soup = BeautifulSoup(url.content, "html.parser")
result = soup.find('span', {'class':'price-tag-fraction'})
price_text = result.text

print("The price is " + price_text)
