from bs4 import BeautifulSoup
from html_loader import load_html


def get_deezer_chart():
    url = 'https://www.deezer.com/en/playlist/3155776842'
    response = load_html(url, length=1000000, timeout=20)
    soup = BeautifulSoup(response, 'lxml')
    table = soup.find('div', class_='datagrid-container')

    names_tags = table.find_all('a', class_='datagrid-label datagrid-label-main title')
    names = []
    for tag in names_tags:
        names.append(tag.get_text())
    # print(len(names), names)

    artists_tags = table.find_all('div', class_='datagrid-cell cell-artist')
    artists = []
    for tag in artists_tags:
        artists.append(tag.get_text().split(', '))
    # print(len(artists), artists)

    album_tags = table.find_all('div', class_='datagrid-cell cell-album')
    album = []
    for tag in album_tags:
        album.append(tag.get_text())
    # print(len(album), album)

    time_tags = table.find_all('div', class_='datagrid-cell cell-duration')
    time = []
    for tag in time_tags:
        time.append(tag.get_text()[1:])
    # print(len(time), time)

    deezer_list = []
    for i in range(len(names)):
        temp = {'service': 'deezer',
                'rank': str(i + 1),
                'name': names[i],
                'artists': artists[i],
                'streams': None,
                'duration': time[i],
                'album': album[i]}
        deezer_list.append(temp)
    # print(deezer_list)
    return deezer_list


# test = get_deezer_chart()
# print(test)
