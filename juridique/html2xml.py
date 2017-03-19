from bs4 import BeautifulSoup

f = open('Portail_Droit français_Arborescence — Wikipédia.html')
soup = BeautifulSoup(f)


#print(soup.find_all('div',class_="CategoryTreeChildren"))
    #print(link.get_text())

for child in soup.find_all('div',class_="CategoryTreeChildren"):
    if not child.div:
        print(child.previous_sibling)