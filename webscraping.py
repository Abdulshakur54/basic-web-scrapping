# import libraries
import requests
from bs4 import BeautifulSoup
import csv

webpage = "http://quotes.toscrape.com"

# send a GET request to the webpage
page = requests.get(webpage)

# ensure the request was successful
if page.status_code == 200:
    # parse the page content
    soup = BeautifulSoup(page.content, 'html.parser')
    quotes = []
    authors = []
    tags = []
    # find the quotes
    quote_containers = soup.find_all('div', class_='quote')
    for quote_container in quote_containers:
        quote = quote_container.find('span', class_='text')
        quotes.append(quote.text)
        author = quote_container.find('small', class_='author').text
        authors.append(author)
        tag_containers = (quote_container.find_all('a', class_='tag'))
        tag_list = [x.text for x in tag_containers]
        tag = '|'.join(tag_list)
        tags.append(tag)
    quote_contents = list(zip(quotes, authors, tags))
    # create a CSV file
    with open('quotes.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        # write the header
        writer.writerow(['Quote', 'Author', 'Tags'])
        # write the data
        writer.writerows(quote_contents)