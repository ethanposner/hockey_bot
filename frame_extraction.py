from data_downloading import download_data
import cv2

def frame_extraction(video_path):
    video = cv2.VideoCapture(video_path)
    frame_count = 0
    success = 1
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

    while success:
        success, frame = video.read()
        if not success:
             break
        cv2.imwrite(f"frame_count_{frame_count}.jpg", frame)
        frame_count += 1

        if frame_count % 100 == 0:  
                print(f"Frames extracted: {frame_count}/{total_frames}")
    
    video.release() 

if __name__ == "__main__":
    video_link = 'https://www.youtube.com/watch?v=bZdFQudDDnc&t=1767s'
    output_path = r"C:\Users\ethan\OneDrive\Hockey Bot"

    video_path = download_data(video_link, output_path)
    
    if video_path:
        frame_extraction(video_path)
    else:
        print("Failed to download video. Exiting.")



