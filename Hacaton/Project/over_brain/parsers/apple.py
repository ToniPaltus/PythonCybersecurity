from bs4 import BeautifulSoup as BS
from html_loader import load_html


def get_apple_chart():
    apple = list()
    url = 'https://music.apple.com/us/playlist/top-100-usa/pl.606afcbb70264d2eb2b51d8dbcfa6a12'
    response = load_html(url, length=1_800_000, timeout=10)
    soup = BS(response, 'lxml')
    songs_list = soup.find('div', attrs={'class': 'songs-list typography-callout'})
    songs = songs_list.find_all('div', attrs={
        'class': 'songs-list-row songs-list-row--web-preview web-preview songs-list-row--two-lines songs-list-row--song'})
    for song in songs:
        rank = song.find('div', class_='songs-list-row__rank').text
        name = song.find('div', class_='songs-list-row__song-name').text
        artists_list = song.find('div', class_='songs-list__song-link-wrapper')
        album = song.find('a', class_='songs-list-row__link').text
        artists = [artist.text for artist in artists_list.find_all('a', class_='songs-list-row__link')]
        duration = song.find('div', class_='songs-list-row__length').text.strip()
        song_dict = {'service': 'apple',
                     'rank': rank,
                     'name': name,
                     'artists': artists,
                     'duration': duration,
                     'album': album,
                     'streams': None, }
        apple.append(song_dict)
    return apple
