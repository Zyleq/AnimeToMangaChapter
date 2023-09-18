import requests
from bs4 import BeautifulSoup

response = requests.get("https://listfist.com/list-of-naruto-shippuden-episode-to-chapter-conversion")

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract elements from each class
    col1_elements = [e.text.strip() for e in soup.select('td.col-1.odd')]
    col2_elements = [e.text.strip() for e in soup.select('td.col-2.even')]
    col3_elements = [e.text.strip() for e in soup.select('td.col-3.odd')]

    # Combine them into pairs
    pairs = list(zip(col1_elements, col2_elements, col3_elements))

    # Print each pair, and after every 3 pairs, add a separator
    for i, pair in enumerate(pairs, 1):
        print(pair)
        if i % 3 == 0:
            print("---")
else:
    print("Failed to retrieve the webpage.")
