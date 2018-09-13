"""Testing the classes"""
from lectures_dothisnow.songs import Song
from lectures_dothisnow.dogs import Dog


def main():
    playlist_songs = []
    song_title = -1
    count = 1
    while song_title != "":
        song_title = input("Enter is the title of the song: ")
        song_artists = input("Enter is the artist of the song: ")
        song_duration = float(input("Enter is the duration of the song: "))
        song = Song(song_title, song_artists, song_duration)
        playlist_songs.append(song)

    # dog_breed = input("Enter is the title of the song: ")
    # dog_age = int(input("Enter is the artist of the song: "))
    # dog_sex = input("Enter is the duration of the song: ")

    for i in range(len(playlist_songs)):
        print(i+1)
main()