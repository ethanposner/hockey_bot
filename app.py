from data_downloading import download_data
from frame_extraction import frame_extraction

def main():
    video_link = 'https://www.youtube.com/watch?v=bZdFQudDDnc&t=1767s'
    output_path = r"C:\Users\ethan\OneDrive\Hockey Bot"
    video_path = download_data(video_link, output_path)

    if video_path:
        frame_extraction(video_path)
    else:
        print("No frames", video_path)

if __name__ == "__main__":
    main()
