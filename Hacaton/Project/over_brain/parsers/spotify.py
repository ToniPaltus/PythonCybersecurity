from bs4 import BeautifulSoup
from html_loader import load_html


def get_spotify_chart():
    url = 'https://spotifycharts.com/regional/global/weekly/2021-08-06--2021-08-13'
    response = load_html(url, length=1000000)
    soup = BeautifulSoup(response, 'lxml')
    table = soup.find('table', class_='chart-table')

    top_position_tags = table.find_all('td', class_='chart-table-position')
    top_positions = []
    # print(top_position_tags)
    for position in top_position_tags:
        top_positions.append(position.get_text())
    # print(top_position)

    top_track_name_tags = table.find_all('td', class_='chart-table-track')
    top_track_name = []
    top_authors_name = []
    # print(top_track_name_tags)
    for name in top_track_name_tags:
        track_name = name.find('strong')
        author_name = name.find('span')

        top_track_name.append(track_name.get_text())
        top_authors_name.append(author_name.get_text().split(', '))
    # print(top_track_name)
    # print(top_authors_name)

    top_stream_tags = table.find_all('td', class_='chart-table-streams')
    top_streams = []
    # print(top_stream_tags)
    for stream in top_stream_tags:
        top_streams.append(stream.get_text())
    # print(top_streams)

    spotify_list = []
    for i in range(len(top_positions)):
        temp = {
                'service': 'spotify',
                'rank': str(top_positions[i]),
                'name': top_track_name[i],
                'artists': top_authors_name[i],
                'streams': top_streams[i],
                'duration': None,
                'album': None}
        spotify_list.append(temp)
    # print(spotify_list)

    return spotify_list




