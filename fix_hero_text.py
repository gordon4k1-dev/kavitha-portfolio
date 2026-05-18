import re

with open('index.html', 'r') as f:
    html = f.read()

# The hero text has `opacity-0` maybe? Let's check the HTML for "PRACTICUM ARCHIVE"
print("PRACTICUM ARCHIVE" in html)
# It's there, but let's check its classes.
import bs4
soup = bs4.BeautifulSoup(html, 'html.parser')
h1 = soup.find('h1', class_='hero-title')
if h1:
    print(h1['class'])
