from pytube import YouTube, Playlist
from os import getcwd

def progressbar(stream, chunk: bytes, bytes_remaining: int):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percent = float(bytes_downloaded / total_size * 100)
    remaining = round(33 - percent//3)
    progress_bar = "▒" * int(percent//3) + " " * remaining
    print(f"\rProgress|{progress_bar}|{percent:05.2f}% ", end='')


def start():
    print("~Welcome to the YouTube video downloader~")
    print("mode: '1' - a video")
    print("      '2' - a playlist")
    print("type: 'a' - mp3")
    print("      'b' - mp4")
    mode = input("\nChoose a mode (1a, 1b, 2a, or 2b): ")

    if mode[0]=='1':
        url = input("Enter the url of the video / 輸入影片的網址 :")
        a_video(url, mode[1])
    elif mode[0]=='2':
        url = input("Enter the url of the playlist / 輸入播放清單的網址 :")
        a_playlist(url, mode[1])
    else:
        print("Wrong mode!")
        quit()

        

def a_video(url, type):
    try:
        yt = YouTube(url, on_progress_callback=progressbar)
    except:
        print("The video's url is unavailable!")
        quit()

    if type=='a':
        target = yt.streams.get_audio_only()
        filename = yt.title + ".mp3"
    elif type=='b':
        target = yt.streams.get_highest_resolution()
        filename = yt.title + ".mp4"
    else:
        print("Wrong mode!")
        quit()
    
    try:
        print("Downloading...")
        dir = getcwd() + "/downloaded_videos"
        target.download(output_path=dir, filename=filename)
        print("\nDone!!")
    except:
        print(f"The video '{yt.title}' can't download!")
        quit()



def a_playlist(url, type):
    try:
        playlist = Playlist(url)
    except:
        print("The playlist's url is unavailable!")
        quit()
        
    if type=='a':
        for url in playlist.video_urls:
            yt = YouTube(url, on_progress_callback=progressbar)
            target = yt.streams.get_audio_only()
            try:
                print("Downloading...")
                dir = getcwd() + "/downloaded_playlist"
                target.download(output_path=dir, filename=yt.title + ".mp3")
                print(f"\n'{yt.title}' -> Done!\n")
            except:
                print(f"The video '{yt.title}' can't download!\nContinue with the next one...\n")
                continue
            
    elif type=='b':
        for url in playlist.video_urls:
            yt = YouTube(url, on_progress_callback=progressbar)
            target = yt.streams.get_highest_resolution()
            try:
                print("Downloading...")
                dir = getcwd() + "/downloaded_playlist"
                target.download(output_path=dir)
                print(f"\n'{yt.title}' -> Done!\n")
            except:
                print(f"The video '{yt.title}' can't download!\nContinue with the next one...\n")
                continue
    else:
        print("Wrong mode!")
        quit()
        
    print("All the videos have been downloaded!")



if __name__=='__main__':
    start()
  
