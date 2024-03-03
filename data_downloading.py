from pytube import YouTube
def download_data(video_link, output_path):

    try:
        yt = YouTube(video_link)
    except:
        print('Error')

    video_stream = yt.streams.get_highest_resolution()

    video_stream.download(output_path)

    print("Video downloaded successfully!")

if __name__ == "__main__":
    video_link = 'https://www.youtube.com/watch?v=bZdFQudDDnc&t=1767s'
    output_path = r"C:\Users\ethan\OneDrive\Hockey Bot"
    video_path = download_data(video_link, output_path)
