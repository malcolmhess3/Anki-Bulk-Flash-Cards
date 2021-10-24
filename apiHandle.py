import requests
from bs4 import BeautifulSoup


# res = requests.get("https://jisho.org/api/v1/search/words?keyword=話す")
# print(res.status_code)
# print(res)
# print(res.json())

res2 = requests.get("https://jisho.org/search/%E8%A9%B1%E3%81%99%23sentences")
print(res2.status_code)
print()

soup = BeautifulSoup(res2.content, "html.parser")
kek = soup.find(id="main_results")
kek2 = soup.find_all("ul", "japanese_sentence japanese japanese_gothic clearfix")

# kek3 = kek2[0].span.extract()


print(kek2[0].get_text())
print(kek2[0].prettify())

kek5 = kek2[0].find_all("span", "furigana")

print(kek2[0].find_all("span", "furigana"))
print(kek2[0].get_text())
for x in kek5:
    print(x.get_text())

line = kek2[0].find_all("li")
comp = ""
for l in line:
    print(l)
    tes = l.find(class_="furigana")
    if (tes):
        comp+= l.find(class_="unlinked").get_text()
        comp+= "[" + tes.get_text() + "]"
    else:
        comp += l.get_text()
print(comp)

# print(line)
# line = line.find_next()
# while(line):
#     print(line)
#     line = line.find_next()
