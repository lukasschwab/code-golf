from bs4 import BeautifulSoup as bs
import requests
import csv

'''
This was a fun little script!

The goal was to scrape all of the logos from sportslogos.net to train
better logo classifiers. We aren't the first ones to do this:
@kylemartin1 posted a scraper on GitHub (http://bit.ly/29cUhDa), but
it seems to be defunct.

Our big breakthrough was the realization that, except for the home 
page and the pages describing individual logos, every page we were
scraping was a series of unordered lists with the class 'logoWall.'
Even if it wasn't a list of logos.

This meant we didn't have to worry about the depth of the links,
because we could just parse each of these list pages recursively.
The whole site is just a tree on which I'm performing depth-first
search.
Neat! Thanks, algos!

Can be improved with serious parallelization.

Outputs results to logos.csv in same directory.
'''

BASE_URL = "http://www.sportslogos.net/"

# Counters
finalPagesReached = 0
currentList = ""

# Prevent infinite loops, retracing
visited = set()
visited.add('http://www.sportslogos.net/index.php')
visited.add('http://www.sportslogos.net/')

# Generic request handler
def handleUrl(url):
	global visited
	if url not in visited and '#' not in url:
		visited.add(url)
		r = requests.get(url).text
		if not isFinalPage(r):
			parseListPage(r)
		else:
			handleFinalPage(r, url)
	else:
		print '\033[93m REJECTED DUPE: \033[0m' + url

# Recurses through all list items on list
# Can be leagues, teams, logos, etc.
def parseListPage(r):
	# Get the list
	soup = bs(r)
	# Get title of working list
	title = soup.find_all('title')[0].text.split(' - ')[0].upper()
	global currentList
	currentList = title
	print '\033[94m NOW HANDLING ' + currentList + '\033[0m'
	# Recurse through items in list
	lists = bs(r).find_all('ul', 'logoWall')
	for l in lists:
		links = l.find_all('a', href=True)
		[handleUrl(BASE_URL + link['href']) for link in links]

# Handles page highlighting image
def handleFinalPage(r, url):
	global finalPagesReached
	global currentList
	finalPagesReached += 1
	soup = bs(r)
	# Get image description
	logo_div = soup.find_all('div', attrs={'class': 'mainLogo'})[0]
	logo = logo_div.find_all('img')[0]
	logo_desc = logo['title']
	logo_url = logo['src']
	# Compile attrs
	attrs = [currentList, url, logo_desc, logo_url]
	# Logging
	print '\033[92m' + str(finalPagesReached) + ': \033[0m' + logo_desc
	with open('sports.csv', 'a') as out:
		wr = csv.writer(out, quoting=csv.QUOTE_ALL)
		wr.writerow(attrs)

# Check if this page has a final logo
def isFinalPage(html):
	mark = "div class=\"mainLogo\" id=\"mainLogo\""
	if mark not in html:
		return False
	else:
		return True

def main():
	home = requests.get('http://www.sportslogos.net/index.php')
	s = bs(home.text)
	s = s.find_all("div", attrs={"id":"footer"})[0]
	sportLinks = s.find_all('ul')[1].find_all('a')
	[handleUrl(BASE_URL + link['href']) for link in sportLinks]

main()
