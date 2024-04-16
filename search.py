import requests
from bs4 import BeautifulSoup

def get_president_info(country):
    # Format the URL to match the Wikipedia page for the specified country
    url = f'https://en.wikipedia.org/wiki/{country.replace(" ", "_")}'

    try:
        # Make a request to get the page content
        response = requests.get(url)
        response.raise_for_status()  # Raises an exception for 4XX or 5XX status codes

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Search for the current president by looking for a relevant section
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
                        print(f"President of {country}: {name}")
                        return
        print("President information not found.")
    except requests.HTTPError as e:
        print(f"Failed to retrieve data: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    while True:
        print("\nWikipedia President Search")
        print("Type 'exit' to quit the program.")
        country = input("Enter the name of the country to find its president: ")
        if country.lower() == 'exit':
            break
        get_president_info(country)

if __name__ == '__main__':
    main()
