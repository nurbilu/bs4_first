# Wikipedia President Search Tool
    This project contains Python scripts that allow you to search for the president of any country using Wikipedia. The scripts use web scraping techniques to extract information directly from the Wikipedia pages of specified countries.

## Getting Started
    These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
The scripts are written in Python and use several external libraries. You will need Python installed on your machine. Python 3.6 or higher is recommended.

### Installing
First, clone the repository or download the files to your local machine. Navigate to the directory containing the files.

To install the necessary Python libraries, run the following command in your terminal:

#### bash
    ```Copy code
    pip install -r requirements.txt
    ```
### File Descriptions
    app.py: This script allows users to input a country name and fetches the president of that country from its Wikipedia page.
    search.py: A helper script that contains the function to extract president information from a given Wikipedia page.
    requirements.txt: Lists all the Python libraries that need to be installed.
### How to Run
    Ensure you are in the project directory. You can start the application by running one of the Python scripts. For example:

    bash
    ```python app.py
    ```
Follow the on-screen prompts to enter the name of the country for which you want to find the president.

### Built With
    Python - The programming language used
    Requests - Used to handle HTTP requests
    Beautiful Soup 4 - Used to parse HTML and XML documents
    
### License
    This project is licensed under the MIT License - see the LICENSE file for details

### Acknowledgments
    Wikipedia for providing the data used by the scripts.
    Python community for the excellent tools and libraries.