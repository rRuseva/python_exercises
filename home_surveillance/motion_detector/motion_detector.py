import cv2
import os
# import sys
# import argparse
# import numpy as np
from datetime import datetime
import time
import pandas as pd
import config as cfg 
import file_manager

# print(sys.version)
# print(cv2. __version__)



if __name__ == '__main__':

    # ap = argparse.ArgumentParser(description="motion detection")
    # ap.add_argument("-v", "video_file", required=False, help="path to the video file.")
    # ap.add_argument("-a", "--min_area", required=False, type=int, default=500, help="minimum detection area")
    # args = ap.parse_args()

    # if args.video_file is not None:
        # video_path  = args.video ### or camera ip  or port number
    
    # import pdb
    # pdb.set_trace
    
    ### initiallizing variables 

    ### get the path to the resulting frames and videos
    dest_path = file_manager.result_dir

    size = cfg.resolution 
    min_area = cfg.min_area
    diff_thresh = cfg.diff_thresh

    initial_frame = None
    time_stamp = []
    status_list = [None, None]
    
    df = pd.DataFrame(columns=["Start", "End"])
    
    vid = cv2.VideoCapture(0)
    time.sleep(2.0)
    # if(vid.isOpened() ==False):
    #     print("Error starting the camera")
    assert vid.isOpened()
    
    vid.set(3,size[0])
    vid.set(4,size[1])
    
    frames_cnt = 0
    motion_cnt = 0

    while(True):   
        ret, frame = vid.read()
        if frame is None:
            break
        ### flag for motion status 
        status = 0
        frame = cv2.flip(frame, 1)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray,(21,21),0)
        
        # save the base frame  
        if initial_frame is None or frames_cnt % 450 == 0:
            initial_frame = gray
            cv2.imshow("initial frame", initial_frame)
        

        delta_frame = cv2.absdiff(initial_frame,gray)
        thresh_frame = cv2.threshold(delta_frame, diff_thresh, 255, cv2.THRESH_BINARY)[1]

        thresh_frame = cv2.dilate(thresh_frame, None,iterations=5)
        (cnts,_) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        for contour in cnts:
            if cv2.contourArea(contour) < min_area:
                continue
            status = 1
            (x,y,w,h)=cv2.boundingRect(contour)
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2) 
        status_list.append(status)
        
        if status_list[-1] == 1 and status_list[-2] == 0:
            time_stamp.append(datetime.now())
            motion_cnt = motion_cnt+1
        
        if status_list[-1] == 0 and status_list[-2] == 1:
            time_stamp.append(datetime.now())
            initial_frame == None


        if status == 1:
            cv2.imwrite(os.path.join(dest_path, str(motion_cnt)+"_frame_"+str(frames_cnt)+".jpg"),frame)
        cv2.imshow("web cam", frame)
        
        frames_cnt = frames_cnt+1
        
        
        k = cv2.waitKey(30) & 0xff
        if k ==27:
            break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            if status == 1:
                time_stamp.append(datetime.now())
            break
    
for idx in range(0, len(time_stamp)-1,2):
    df = df.append({"Start":time_stamp[idx], "End":time_stamp[idx+1]},ignore_index=True)
    
    df.to_csv(os.path.join(dest_path,"All_Time_Stamps.csv"))

    
    vid.release()
    cv2.destroyAllWindows()