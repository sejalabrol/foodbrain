from bs4 import BeautifulSoup
import lxml
import requests
from lxml import etree

url = "https://www.thescramble.com/glossary-of-cooking-terms/"

response = requests.get(
    url,
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
    },
)

contents = response.text
soup = BeautifulSoup(contents, "lxml")
documentObjectModel = etree.HTML(str(soup))

file1 = open("data/all_terms.txt", "w")
file2 = open("data/all_desc.txt", "w")
file3 = open("data/terms_to_learn.txt", "w")

for i in range(1, 68):
    term_path = f'//*[@id="post-56510"]/div/h4[{i}]'
    desc_path = f'//*[@id="post-56510"]/div/p[{i+1}]'
    term = documentObjectModel.xpath(term_path)[0].text[:-1]  # to remove the semicolon
    desc = documentObjectModel.xpath(desc_path)[0].text
    file1.write(term + "\n")
    file2.write(desc + "\n")
    file3.write(str(i - 1) + "\n")

file1.close()
file2.close()
file3.close()
