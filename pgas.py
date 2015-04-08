import bs4
import requests


url = 'http://www.paulgraham.com/articles.html'


def get_article_urls():
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text)
    articles = soup.findAll('table')[2]
    return [a.get('href') for a in articles.find_all('a')]


if __name__ == "__main__":

    hrefs = get_article_urls()
    links = [l if 'http' in l else 'http://www.paulgraham.com/%s'
             % l for l in hrefs]

    print len(links)
    print '\n'.join(l for l in links)
