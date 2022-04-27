from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
# print(soup.title)
articles = soup.find_all(name="a", class_="titlelink")

article_texts=[]
article_links=[]

for article_tag in articles:
    article_text = article_tag.getText()
    article_texts.append(article_text)

    article_link = article_tag.get("href")
    article_links.append(article_link)


article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name = "span",class_ = "score")]


print(article_texts)
print(article_links)
print(article_upvotes)


# 查找最大数值
largest_number = max(article_upvotes)
print(largest_number)
# 获得索引
largest_index = article_upvotes.index(largest_number)
print(largest_index)
#打印标题，但是需要+1
print(article_texts[int(largest_index+1)])








# with open("website.html") as file:
#     contents = file.read()
#
#
# soup = BeautifulSoup(contents, "html.parser")


# print(soup.title)
# <title>Angela's Personal Site</title>
# print(soup.title.name)
# title
# print(soup.title.string)
# Angela's Personal Site

# print(soup.prettify())
# 有缩进的html格式

# print(soup.a)
# <a href="https://www.appbrewery.co/">The App Brewery</a>
# print(soup.li)
# <li>The Complete iOS App Development Bootcamp</li>
# print(soup.p)
# <p><em>Founder of <strong><a href="https://www.appbrewery.co/">The App Brewery</a></strong>.</em></p>

#但是只展示第一个
# 可以用 find_all()

# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

# for tag in all_anchor_tags:
    # print(tag.getText())
    # print(tag.get("href"))


# heading = soup.find(name = "h1",id="name")
# print(heading)
# print(heading.getText())
#
# section_heading = soup.find(name = "h3",class_="heading")
# print(section_heading)
# print(section_heading.getText())
# print(section_heading.get("class"))
#
# company_url = soup.select_one(selector="p a")
# print(company_url)
#
# name = soup.select_one(selector="#name")
# print(name)
#
# headings = soup.select(".heading")
# print(headings)



