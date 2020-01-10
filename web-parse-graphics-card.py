# Web Parsing

from bs4 import BeautifulSoup as soup  # HTML data structure
# urllib is package; request is module; urlopen is function which is renamed as uReq
from urllib.request import urlopen as uReq  # Web client

# URl to web scrap from.
# in this example we web scrap graphics cards from Newegg.com
my_url = 'https://www.newegg.com/global/au-en/p/pl?d=graphics+card&N=100203018&name=Desktop%20Graphics%20Cards&isdeptsrh=1'

# opens the connection and downloads html page from url
uClient = uReq(my_url)

# parses html into a soup data structure to traverse html
# as if it were a json data type.
page_soup = soup(uClient.read(), "html.parser")
uClient.close()

# finds each product from the store page
containers = page_soup.findAll("div", {"class": "item-container"})

# name the output file to write to local disk
out_filename = "graphics_cards.csv"
# header of csv file to be written
headers = "Brand,Name,Price \n"

# opens file, and writes headers
f = open(out_filename, "w")
f.write(headers)

# loops over each product and grabs attributes about
# each product
for container in containers:
	
	# try:
	# 	brand_container = container.find("div", "item-info")
	# 	product_brand = brand_container.div.a.img["title"]

	# 	price_container = container.findAll("li", {"class": "price-current"})
	# 	price_numbers_containers = (price_container[0].findAll("strong"))
	# 	product_price = price_numbers_containers[0].text

	# except Exception as e:
	# 	product_brand = "NA"
	# 	product_price = "NA"

	# else:
	# 	pass
	# finally:
	# 	pass

	brand_container = container.find("div", "item-info")
	# product_brand = brand_container.div.a.img["title"]
	if brand_container.div.a.img == None: 
		continue
	else:

		product_brand = brand_container.div.a.img["title"]
		
		price_container = container.findAll("li", {"class": "price-current"})
		price_numbers_containers = (price_container[0].findAll("strong"))
		product_price = price_numbers_containers[0].text

		title_container = container.findAll("a", {"class": "item-title"})
		product_name = title_container[0].text


		# prints the dataset to console
		print("Brand: " + product_brand)
		print("Name: " + product_name)
		print("Price: $" + product_price + "\n")

		# writes the dataset to file
		# Concatenate with a comma in the middle (seperate columns using commas)
		f.write(product_brand + ", " + product_name.replace(",", "|") + ", " + product_price.replace(",", "") + "\n")

f.close()
