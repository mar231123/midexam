print("Qusetion no 03")
class song:
    def __init__(self,title,artist,album,duration):
        self.title=title
        self.artist=artist
        self.album=album
        self.duration=duration
class playlist():
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.songs = []
    def add_song(self, song):
        self.songs.append(song)
    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
        else:
            print(f"{song.title} is not in the playlist.")
    def display_songs(self):
        print(f"Playlist: {self.title} - {self.description}")
        for song in self.songs:
            print("-", song)

class MusicLibrary:
    def __init__(self):
        self.playlists = []
    def add_playlist(self, playlist):
        self.playlists.append(playlist)
    def remove_playlist(self, playlist):
        if playlist in self.playlists:
            self.playlists.remove(playlist)
        else:
            print(f"{playlist.title} is not in the library.")
        self.playlists.remove(playlist)
    def display_playlists(self):
        for playlist in self.playlists:
            print(f"Playlist: {playlist.title}")
            print(f"Description: {playlist.description}")
            print("Songs:")
            playlist.display_songs()
            print("\n")
song1 = song("Shape of You", "Ed Sheeran", "÷", 233)
song2 = song("Someone Like You", "Adele", "21", 285)
song3 = song("Bohemian Rhapsody", "Queen", "A Night at the Opera", 354)
playlist1 = playlist("Favorites", "My favorite songs")
playlist1.add_song(song1)
playlist1.add_song(song2)
playlist2 = playlist("Classics", "Classic hits")
playlist2.add_song(song3)
library = MusicLibrary()
library.add_playlist(playlist1)
library.add_playlist(playlist2)
library.display_playlists()
library.remove_playlist(playlist2)
library.display_playlists()


