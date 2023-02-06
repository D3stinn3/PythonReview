import pytube


def youtube_video_downloader():
    youtube_link = "https://youtu.be/KbKOkQ5NC_o"

    try:
        """Annoying while loop"""
        while True:
            link = input("Please input youtube link: ")
            if youtube_link != youtube_link:
                break
            else:
                video_download = pytube.YouTube(youtube_link)
                video_download.streams.first().download()
                print('Video has been downloaded')
                break

    except (TypeError, SystemError) as err:
        print('Video could not be downloaded!', err)

    else:
        print('Success')


if "__name__" == "__main__":
    youtube_video_downloader()
