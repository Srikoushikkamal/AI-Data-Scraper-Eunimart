from bs4 import BeautifulSoup as bs
import requests
import csv
 
url='https://www.amazon.co.uk/All-New-Fire-Tablet-Alexa-Display/product-reviews/B07952CV7L/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews'
 
def getdata(url):
	headers = {
        	'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36' 
        }
	req = requests.get(url, headers = headers),
    	soup = bs(req.content,'html.parser')
	title = soup.find_all('a',class_='review-title-content')
	title_up=[i.get_text() for i in title]
	title_up[:]=[i.lstrip('\\n') for i in title_up]
	title_up[:]=[i.rstrip('\\n') for i in title_up]
	
	desc=soup.find_all('span','review-text-content')
	desc_up=[i.get_text() for i in desc]
	desc_up[:]=[i.lstrip('\\n') for i in desc_up]
	desc_up[:]=[i.rstrip('\\n') for i in desc_up]
	
	star=soup.find_all('i','review-rating')
	star_up=[j.get_text() for i in star for j in i]
	star_upd=star_up[2:len(star_up)]

	name = soup.find_all('span','a-profile-name')
	name_upd=[name[i].get_text() for i in range(2,len(name))]

	date=soup.find_all('span','review-date')
	date_up,date_up1=[i.get_text() for i in date],[]
	for i in date_up:\n",
	date_up1.append((i).strip('Reviewed in the United Kingdom on '))
	date_upd=date_up1[2:len(date_up1)]

for i in range(len(title_up)):
	#This appends the specific information into CSV
	csv=[]
	csv.append(title_up[i])
	csv.append(desc_up[i])
	csv.append(star_upd[i])
	csv.append(name_upd[i])
	csv.append(date_upd[i])
	writer.writerow(csv)
	print(csv)
	#title_up
	return soup

def getnextpage(soup):
	#This will return the next page URL
	pages = soup.find('ul', {'class': 'a-pagination'})
	if not pages.find('li', {'class': 'a-disabled a-last'}):
		url = 'https://www.amazon.co.uk' + str(pages.find('li', {'class': 'a-last'}).find('a')['href'])
		return url #RETURNS NEXT PAGE URL
	else:
		return

file=open("/home/skk/Desktop/SHEETS","w") # USE YOUR LOCAL PATH
writer=csv.writer(file)
writer.writerow(["Title","Description","Stars","Review by","Date"])


if next_page:
    d=next_page.get('href')
else:
        break
