import os
from functions.pathConfig import get_default
def chop_files():
    default_path = get_default()
    for files in os.listdir(f"{default_path}/autoScroll/autoScrollResults"):
        
        count = 0
        ext = os.path.splitext(files)[-1].lower()
        
        if ext == ".mkv":
            os.system(f'ffmpeg -i "{default_path}/autoScroll/autoScrollResults/{files}" -c copy -map 0 -segment_time 00:00:45 -f segment -reset_timestamps 1 C:/Users/Jonah/Downloads/Projects/autoScroll/Outputs/output{count}%03d.mp4')
            os.remove(f"{default_path}/autoScroll/autoScrollResults/{files}")
            count += 1


