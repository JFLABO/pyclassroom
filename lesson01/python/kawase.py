import urllib.request

from bs4 import BeautifulSoup

from datetime import datetime

import os



# Ignore SSL_CERTIFICATE for https

import ssl

ssl._create_default_https_context = ssl._create_unverified_context
print("\007")


# Yahoo finance

url = "https://stocks.finance.yahoo.co.jp/stocks/detail/?code=USDJPY=X&serviceKanriId=USDJPY=X&pos=1&ccode=ofv"

# Data file

file_name = '/home/test/usd.csv'



# Make data elements for first execution

if os.path.exists(file_name):

	pass

else:

	element = "year,month,day,hour,minute,usd,\n"

  	#with open(file_name, mode='w') as f:

    	#	f.write(element)



def main():

	# Scraping

	response = urllib.request.urlopen(url)

	soup = BeautifulSoup(response, 'html.parser')

	# US doll rate

	td = soup.find("td", class_="stoksPrice")

	

	# Time to confirm this program successed

	now = datetime.now()

	

	# Save usd to csv file

  	#with open(file_name, mode='a') as f:

    	#	f.write('{},{},\n'.format(now.strftime("%Y,%m,%d,%H,%M"),td.string))



main()
