from bs4 import BeautifulSoup
from urllib import request
import requests


def make_soup(url):
    html = request.urlopen(url).read()
    return BeautifulSoup(html)


def get_photos(url, img_link):
    with requests.Session() as c:
        c.get(url)
        c.headers.update({'referer': url})
        res = c.get(img_link)
        if res.status_code == 200:
            return res.content


def get_image_name(url):
    url = url.split("/")
    return "Data/image{}.jpeg".format(url[-2])


def load_images_from_album(url):
    soup = make_soup(url)
    images = soup.find_all("img", {"class": "autocover image__img image__landscape", "class" : "autocover image__img image__portrait"})
    image_count = 0
    for image in images:
        image_source = "https:{}".format(image.get("data-src"))
        print(image_source)
        with open(get_image_name(image_source), 'wb') as f:
            f.write(get_photos(url, image_source))
        image_count = image_count + 1
    print("{} images loaded".format(image_count))


def main():
    urls = [
    ]
    for url in urls:
        load_images_from_album(url)


if __name__ == "__main__":
    main()
