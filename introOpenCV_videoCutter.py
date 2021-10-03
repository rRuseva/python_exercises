import cv2
import os
import sys
import argparse
import numpy as np
from datetime import datetime 


def video_cutter(video_path, video_name, start, end):

    video_obj = cv2.VideoCapture(os.path.join(video_path, video_name))
    

    if (video_obj.isOpened() == False):
        print("ERROR opening the file! Please, close all windows.")

    # get video metadata as video resolution, frame rate, lenght;
    # get the time stamp of the current frame to use it in the file name
    fps = video_obj.get(cv2.CAP_PROP_FPS)
    video_codec = video_obj.get(cv2.CAP_PROP_FOURCC)


    total_frame_count = video_obj.get(cv2.CAP_PROP_FRAME_COUNT)
    video_duration = float(total_frame_count / fps)
    width = video_obj.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = video_obj.get(cv2.CAP_PROP_FRAME_HEIGHT)


    print("reading...: \n\tname:\t\t{} \n\tresolutuion:\t{}x{} \n\tfps:\t\t{} \n\tlenght:\t\t{}sec ({} frames) \n  ".format(
        video_name, int(width), int(height), fps, int(video_duration), int(total_frame_count)))

    start_sec = get_seconds(start)

    end_sec = get_seconds(end)

    if end == None :
        end_sec = video_duration
    else: end_sec = get_seconds(end) 


    start_frame = int( start_sec * fps) 
    end_frame = int( end_sec * fps) 

    if start_frame > end_frame:
        print("Error: end timecannot be before start time")
    
    print("{}-{}".format(start, start_frame))
    print("{}-{}".format(end, end_frame))

    # start_frame = int(get_seconds(start) * fps)
    # end_frame = int(get_seconds(end) * fps)
    video_name = video_name.split('.')
    new_video_name = os.path.join(video_path, video_name[0]+"_new."+video_name[1]) #video_name+"_new" ### o
    print(new_video_name)
    print(int(video_codec))
    out = cv2.VideoWriter(new_video_name, int(video_codec),int(fps),(int(width),int(height)))

    # video_obj.set(1,start_frame)
    # ret,frame = video_obj.read()
    # if frame is not None:
    #     cv2.imshow("frame_{}".format(start), frame)

    # video_obj.set(1,end_frame)
    # ret,frame = video_obj.read()
    # if frame is not None:
    #     cv2.imshow("frame_{}".format(end), frame)

    curr_pos = start_frame
    for i in range(start_frame,end_frame):
        video_obj.set(1,i)
        ret,frame = video_obj.read()
        if ret == True:
            # cv2.imshow("frame_{}".format(i), frame)
            out.write(frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
              break
        else:
            break

    video_obj.release()
    out.release()
    #     curr_pos += 1

    # curr_frame = int(total_frame_count / 2 - N / 2)
    # for i in range(curr_frame, curr_frame + N):
    #     video_obj.set(1, curr_frame)
    #     ret, frame = video_obj.read()
    #     time_stamp = round(float(i / fps), 2)
    #     # cv2.imshow("frame_{}_{}".format(time_stamp, i), frame,)
    #     print("frame saved:\n\t{}{}_frame_{}.{}".format(dest_path, video_name, time_stamp, frame_ext))
    #     cv2.imwrite(dest_path + video_name + "_frame_{}.{}".format(time_stamp, frame_ext), frame)
    #     # curr_frame += i

    # print("__________________________\n")
    # # Wait for a keypress
    # cv2.waitKey(0)

    # Clean up
    cv2.destroyAllWindows()

def get_seconds(time_str):
    # print('Time in hh:mm:ss:', time_str)
    # split in hh, mm, ss
    hh, mm, ss = time_str.split(':')
    
    return int(hh) * 3600 + int(mm) * 60 + int(ss)


if __name__ == '__main__':

    
    ap = argparse.ArgumentParser(description="Trim video by start and end time.")
    ap.add_argument("video", help="specify the video file with absolute path.")
    ap.add_argument("-s", "--start_time", required=False, type=str, default=0, help="Start time of the new video; If not given, the beggining of the original video is set as start_time")
    ap.add_argument("-e", "--end_time", required=False, type=str, default=None, help="Ed time of the new video; If not given, the end of the original file is set as end_time")

    args = ap.parse_args()

    video_path = args.video

    # import ipdb
    # ipdb.set_trace()

    if not os.path.exists(video_path):
        raise FileNotFoundError("File not found")

    current_dir = os.path.dirname(video_path)
    video_name = os.path.basename(video_path)

    # start = datetime.strptime(args.start_time, "%H:%M:%S") 
    # if args.end_time is not None:
    #     end = datetime.strptime(args.end_time, "%H:%M:%S")     
    #     if start > end:
    #         print("Start time cannot be greater than end time")

    start = args.start_time
    if args.end_time is not None:
        end = args.end_time
        # if start > end:
        #     print("Start time cannot be greater than end time")

    video_cutter(current_dir,video_name, start, end)
