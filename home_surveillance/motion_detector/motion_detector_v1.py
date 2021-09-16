import cv2
import os
import sys
import argparse
import numpy as np
from datetime import datetime
import pandas as pd
import time

print(sys.version)
print(cv2. __version__)



if __name__ == '__main__':

    # ap = argparse.ArgumentParser(description="motion detection")
    # ap.add_argument("-v", "video_file", required=False, help="path to the video file.")
    # ap.add_argument("-a", "--min_area", required=False, type=int, default=500, help="minimum detection area")
    # args = ap.parse_args()

    # if args.video_file is not None:
        # video_path  = args.video ### or camera ip  or port number
    
    dest_path = ""
    size = (640, 480)
    min_area = 5000
    initial_frame = None
    time_stamp = []
    status_list = [None, None]
    df = pd.DataFrame(columns=["Start", "End"])
    
    vid = cv2.VideoCapture(0)
    time.sleep(2.0)
    if(vid.isOpened() ==False):
        print("Error starting the camera")
    
    vid.set(3,size[0])
    vid.set(4,size[1])
    
    # result = cv2.VideoWriter(dest_path+'filename.avi', cv2.VideoWriter_fourcc(*'MJPG'), 10, size)
    i = 0
    start_time=0
    end_time =0 
    while(True):
        
        ret, frame = vid.read()
        if frame is None:
            break
        status = 0
        frame = cv2.flip(frame, 1)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray,(21,21),0)
        
        # save the first frame 
        if initial_frame is None:
            initial_frame = gray
            cv2.imshow("init frame", initial_frame)

        delta_frame = cv2.absdiff(initial_frame,gray)
        thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]

        thresh_frame = cv2.dilate(thresh_frame, None,iterations=3)
        (cnts,_) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        for contour in cnts:
            if cv2.contourArea(contour) <min_area:
                continue
            status = 1
            (x,y,w,h)=cv2.boundingRect(contour)
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2) 
            
        
        status_list.append(status)
        if status_list[-1] == 1 and status_list[-2] == 0:
            time_stamp.append(datetime.now())
            start_time = datetime.now()
        
        if status_list[-1] == 0 and status_list[-2] == 1:
            time_stamp.append(datetime.now())
        

        if i % 120 == 0:
            cv2.imwrite(dest_path + str(start_time)+"_frame_"+str(i)+".jpg", frame)
        
        i = i+1 
        cv2.imshow("web cam", frame)
        # result.write(frame)
        
        
        k = cv2.waitKey(30) & 0xff
        if k ==27:
            break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            if status == 1:
                time_stamp.append(datetime.now())
            break
    
    for i in range(0, len(time_stamp),2):
        df = df.append({"Start":time_stamp[i], "End":time_stamp[i+1]},ignore_index=True)
    
    df.to_csv(dest_path+"All_Time_Stamps.csv")

    
    vid.release()
    cv2.destroyAllWindows()