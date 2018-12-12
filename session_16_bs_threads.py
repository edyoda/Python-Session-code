import requests
from bs4 import BeautifulSoup
import threading


def get_deatils(card):
	price = card.find("div",attrs={"class":"m-srp-card__price"})
	title = card.find("a",attrs = {"class":"m-srp-card__title"})

	response2 = requests.get(title.get("href"))
	soup2 = BeautifulSoup(response2.content,"html.parser")
	addr = soup2.find("div",text ="Address")

	addr_value = addr.find_next_sibling("div")
	title_text = title.text.replace("\n"," ")
	super_area = card.find("div",attrs = {"class":"m-srp-card__summary__info"})
	print("{} {} {} {}".format(title_text,price.text,super_area.text,addr_value.text))
	print("------------------------------------------------------------------------")

response = requests.get("https://www.magicbricks.com/property-for-sale/residential-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment&cityName=Bangalore")
soup = BeautifulSoup(response.content,"html.parser")
cards = soup.find_all("div",attrs={"class":"m-srp-card__container"})

cards = soup.find_all("div",attrs={"class":"m-srp-card__container"})

for card in cards:
	t = threading.Thread(target= get_deatils,args=(card,))
	t.start()

    