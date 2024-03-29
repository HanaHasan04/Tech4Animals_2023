import os
from pathlib import Path
import cv2

# each frame is saved as its video name + its index in the video

def extract_and_save_video_frames():
    path = Path('C:/Users/USER/Documents/UniversityProjects/PythonProjects/FinalProject')
    videos_path = Path(os.path.join(path, 'Videos')).glob('*')
    images_path = os.path.join(path, 'Images')
    
    for video_folder in videos_path:
        emotion = os.path.basename(video_folder)
        for video in os.listdir(video_folder):
            video_name = os.path.splitext(video)[0]
            vid = os.path.join(os.path.join(os.path.join(os.path.join(path, "Videos"), emotion)), str(video_name)+".mp4")
            cap = cv2.VideoCapture(vid)
            i = 0
            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break
                img_name = os.path.join(os.path.join(os.path.join(os.path.join(path, "Images"), emotion)),
                                   str(video_name) + '__' + str(i) + '.jpg')
                print(img_name)
                cv2.imwrite(img_name, frame)
                i += 1
    cap.release()
    cv2.destroyAllWindows()

    
if __name__ == '__main__':
    extract_and_save_video_frames()
