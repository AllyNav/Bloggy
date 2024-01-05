import requests
from bs4 import BeautifulSoup
from storeurl import yoururl


#function to extract a only the blog content from a given link
def extract_paragraphs_after_first_header(url):
    # Sending a request to the website
    response = requests.get(url)
    if response.status_code != 200:
        return "Failed to retrieve the web page."

    # Parsing the HTML content of the page
    soup = BeautifulSoup(response.content, "html.parser")

    # Finding all headers and paragraphs
    elements = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p'])

    # Flag to track the encounter of the first header
    found_first_header = False
    content = []

    #Extract Heading h1
    headings= soup.find(['h1'])
    heading_text ="\n".join(heading.get_text() for heading in headings)

    content.append(heading_text)

    for element in elements:
        if element.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6','li']:
            if not found_first_header:
                found_first_header = True
            continue


        if found_first_header and element.name == 'p' or element.name == ['h1','h2', 'h3', 'h4', 'h5', 'h6'] or element.name == 'li' or element.name == 'ul':
            content.append(element.get_text(strip=True))



    return '\n'.join(content)

# URL of the blog post
url = yoururl

# Extracting the paragraph content after the first header
content = extract_paragraphs_after_first_header(url)


#if footer gets in just count the character and change the value of higher bond for new_content
#new_content= content[0:-395]

# Define the filename for saving the content
file_name = "output.txt"

# Writing the content to a file
with open(file_name, 'w', encoding='utf-8') as file:
    file.write(content)

print(content)
#print(f"Content saved to {file_name}")