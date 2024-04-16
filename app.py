import requests
from bs4 import BeautifulSoup

def get_president_info():
    # URL of the Wikipedia page for Iran
    url = 'https://en.wikipedia.org/wiki/Iran'

    # Make a request to get the page content
    response = requests.get(url)
    response.raise_for_status()  # Raises an exception for 4XX or 5XX status codes

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Search for the current president by looking for a relevant section
    # This assumes there's a specific section or paragraph mentioning the president.
    # Adjust the find/search method accordingly if the structure is different.
    infobox = soup.find('table', class_='infobox')
    if infobox:
        # Attempt to find a row labeled 'President' in the infobox
        rows = infobox.find_all('tr')
        for row in rows:
            header = row.find('th')
            if header and 'president' in header.text.lower():
                # Assuming the president's name is listed in the next cell
                name_cell = row.find('td')
                if name_cell:
                    name = name_cell.get_text(strip=True)
                    print(f"President of Iran: {name}")
                    return
    print("President information not found.")

if __name__ == '__main__':
    get_president_info()
