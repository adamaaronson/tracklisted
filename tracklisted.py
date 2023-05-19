import re
import sys
import urllib.request
from bs4 import BeautifulSoup
from dataclasses import dataclass

DISCOGS_TRACK_TITLE = re.compile('^trackTitle')
DISCOGS_DURATION = re.compile('^duration')
DISCOGS_CREDITS = re.compile('^trackCredits')
DISCOGS_LINK = re.compile('^link')
DISCOGS_FEATURING = 'Featuring'

SECS_PER_MIN = 60

@dataclass
class Track:
    title: str
    duration: str
    features: list[str]

def read_html(url: str):
    f = urllib.request.urlopen(url)
    html = f.read().decode('utf-8')
    f.close()
    return html

def get_tracks_from_discogs(html: str):
    soup = BeautifulSoup(html, 'html.parser')

    tracks = []
    tracklist_rows = [row for row in soup.find_all('tr') if row.has_attr('data-track-position')]
    
    for row in tracklist_rows:
        title_spans = row.find_all('span', {'class': DISCOGS_TRACK_TITLE})
        title_tds = row.find_all('td', {'class': DISCOGS_TRACK_TITLE})
        if title_tds:
            title_spans = title_tds[0].find_all('span')
        title = title_spans[0].text.strip()

        duration_tds = row.find_all('td', {'class': DISCOGS_DURATION})
        if duration_tds:
            if duration_tds[0].text:
                duration = duration_tds[0].text
            else:
                duration_spans = duration_tds[0].find_all('span')
                if duration_spans:
                    duration = duration_spans[0].text.strip()
                else:
                    duration = ''
        else:
            duration = ''

        credits = row.find_all('div', {'class': DISCOGS_CREDITS})
        if credits:
            credits_divs = credits[0].find_all('div')
            features_divs = [div for div in credits_divs if DISCOGS_FEATURING in str(div)]
            if features_divs:
                features_links = features_divs[0].find_all('a', {'class': DISCOGS_LINK})
                features = [link.text for link in features_links]
            else:
                features = []
        else:
            features = []

        track = Track(title, duration, features)
        tracks.append(track)
    
    return tracks

def get_total_duration(tracks: list[Track]):
    durations = [track.duration for track in tracks]
    durations = [duration.split(':') for duration in durations]
    durations = [[int(time) for time in duration] for duration in durations]
    mins, secs = zip(*durations)

    total_time_in_secs = sum(mins) * SECS_PER_MIN + sum(secs)
    total_mins = total_time_in_secs // SECS_PER_MIN
    total_secs = total_time_in_secs % SECS_PER_MIN

    return f'{total_mins:02d}:{total_secs:02d}'

def list_to_english(items: list):
    if len(items) < 3:
        return ' and '.join(items)
    else:
        return ', '.join(items[:-1]) + ', and ' + items[-1]

def get_wikipedia_track_listing_template(tracks: list[Track]):
    template = '{{Track listing\n'

    for i, track in enumerate(tracks):
        num = i + 1
        template += f'| title{num} = {track.title}\n'
        if track.duration:
            template += f'| length{num} = {track.duration}\n'
        if track.features:
            features_text = 'feat. ' + list_to_english(track.features)
            template += f'| note{num} = {features_text}\n'

    if all([track.duration for track in tracks]):
        total_length = get_total_duration(tracks)
        template += f'| total_length = {total_length}\n'
    
    template += '}}'

    return template

def main():
    url = sys.argv[1]
    html = read_html(url)
    track_listing = get_tracks_from_discogs(html)
    template = get_wikipedia_track_listing_template(track_listing)
    print(template)

if __name__ == '__main__':
    main()