import random
import os

music_dir = r"C:\Users\destinne\Music\Mymusic"
songs = os.listdir(music_dir)


def music_list():
    for song in songs:
        print(song)


def music_player():
    wimbo = random.randint(0, len(songs))
    print(songs[wimbo])

    os.startfile(os.path.join(music_dir, songs[0]))

    for song in range(0, len(songs)):
        print(song)
        break


if "__name__" == 'main':
    music_player()
    music_list()
