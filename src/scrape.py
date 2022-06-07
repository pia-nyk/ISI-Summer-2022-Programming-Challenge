import json
import requests
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, page, url, articles):
        self.page = page
        self.url = url
        self.articles = articles

    def get_article_content(self, url):
        # make a request to the news article page
        news_page_response = requests.get(url)
        news_page_html = news_page_response.content

        # parse the news html
        data = BeautifulSoup(news_page_html, features='html.parser', from_encoding='ascii')

        # get the img url & caption
        img_url = self.page + data.find('div', {"class": "responsive-image"}).find("img")['src']
        img_caption_tag = data.find('figcaption')
        img_caption = ""

        if img_caption_tag is not None:
            img_caption += img_caption_tag.get_text().encode("ascii", "ignore").decode()

        # get the news content
        content_div = data.find('div', {"class": "wysiwyg--all-content"})
        content = ""
        if content_div is not None:
            content_ps = [p.get_text().lstrip().rstrip() for p in content_div.find_all('p')]

            # append content from all ps in one string
            content += " ".join(content_ps)
            content = content.encode("ascii", "ignore").decode()

        return img_url, img_caption, content

    def process_article_to_json(self, article):
        title = article.find('a').text.encode("ascii", "ignore").decode()
        headline = article.find('p').text.encode("ascii", "ignore").decode()
        footer_content = article.find('footer').find_all('span')
        published_date = footer_content[1].text
        url = (self.page + article.find('a')['href'])

        # open the news article page and get content & picture
        more_details = self.get_article_content(url)

        news_article = {"title": title, "headline": headline, "published_date": published_date, "url": url,
                        "img": more_details[0], "img_caption": more_details[1], "content": more_details[2]}
        return news_article

    def get_news_json(self):
        response = requests.get(self.url)
        html = response.content
        data = BeautifulSoup(html, features='html.parser', from_encoding='ascii')

        # get the featured articles
        parent = data.find('ul', {"class": 'featured-articles-list'})
        featured_articles = parent.find_all('li')

        top_news = []

        # pre-process the features articles
        for article in featured_articles:
            news_article = self.process_article_to_json(article.article)
            top_news.append(news_article)

        # find the remaining articles
        n = self.articles - len(featured_articles)

        # get the remaining articles from news feed
        news_feed_articles_parent = data.find('section', {"id": 'news-feed-container'})
        news_feed_articles = news_feed_articles_parent.find_all('article')[0:n]
        for article in news_feed_articles:
            news_article = self.process_article_to_json(article)
            top_news.append(news_article)

        return {"top_news": top_news}

    def store_data_to_json_file(self):
        # save the output to a file
        with open("../output/news.json", "w") as output_file:
            file_data = json.dumps(self.get_news_json(), indent=2)
            output_file.write(file_data)
