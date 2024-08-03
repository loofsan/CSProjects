# TODO: Import Artist from Artist.py
from Artist import Artist

class Artwork:
    # TODO: Define constructor with parameters to initialize instance attributes
    #       (title, year_created, artist)
    def __init__(self, title='unknown', cre=-1, art=Artist()):
        self.title = title
        self.year_created = cre
        self.artist = art

    def print_info(self):
        self.artist.print_info()
        print(f'Title: {self.title}, {self.year_created}')