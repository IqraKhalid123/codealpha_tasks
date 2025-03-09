import requests
from bs4 import BeautifulSoup
import csv

with open('inspirational_quotes.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Quote', 'Author', 'Tags'])

    url = 'http://quotes.toscrape.com'
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    quotes = soup.find_all('div', class_='quote')
    for quote in quotes:
       tags = [tag.text.lower() for tag in quote.find_all('a', class_='tag')]

       if 'inspirational' in tags:
           text = quote.find('span', class_='text').text
           author = quote.find('small', class_='author').text
    
           writer.writerow([text, author, ', '.join(tags)])
           print(f"Found inspirational quote: {text} by {author}")
           


