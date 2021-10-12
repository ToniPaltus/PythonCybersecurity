from bs4 import BeautifulSoup
from html_loader import load_html

def get_yandex_chart():
    url = 'https://music.yandex.ru/chart'
    response = load_html(url, length=1000000000, timeout=20)
    soup = BeautifulSoup(response, 'lxml')
    table = soup.find('div', class_='lightlist__cont')

    names_tags = table.find_all('div', class_='d-track__name')
    names = []
    for tag in names_tags:
        names.append(tag.get_text())
    #print(names)

    artists_tags = table.find_all('span', class_='d-track__artists')
    artists = []
    for tag in artists_tags:
        artists.append(tag.get_text())
    #print(artists)

    time_tags = table.find_all('span', class_="typo-track deco-typo-secondary")
    time = []
    for tag in time_tags:
        time.append(tag.get_text())
    #print(time)

    yandex_list = []
    for i in range(len(names)):
        temp = {'rank': i + 1,
                'name': names[i],
                'artists': artists[i],
                'streams': None,
                'duration': time[i],
                'album': None}
        yandex_list.append(temp)
    #print(yandex_list)
    return yandex_list

list = get_yandex_chart()
print(list)



