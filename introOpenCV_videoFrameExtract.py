import cv2
import os
import sys
import argparse
import numpy as np

print(sys.version)
print(cv2. __version__)


def listFiles(directory_path):

    videoFileNames = []

    if(not os.path.exists(directory_path)):
        print("(>_<)  Oops! No such directory (-_-)  \n")
        return
    # print("Files for renaming:")
    for fileName in os.listdir(directory_path):
        if (fileName.endswith(".mp4") or fileName.endswith(".MOV")):
            videoFileNames.append(fileName)
        # print(" - " + fileName)

    vCount = len(videoFileNames)  # count renamed video
    if(vCount > 0):
        print("\n")
        print("Processing {} videos".format(vCount))
        print("\n*************************** >^_^< ***************************\n\n")

    return videoFileNames


def FrameExtract(video_path, dest_path, N, frame_ext):

    video_obj = cv2.VideoCapture(video_path)
    video_name = video.split(".")[0]

    if (video_obj.isOpened() == False):
        print("ERROR opening the file! Please, close all windows.")

    # get video metadata as video resolution, frame rate, lenght;
    # get the time stamp of the current frame to use it in the file name
    fps = video_obj.get(cv2.CAP_PROP_FPS)
    total_frame_count = video_obj.get(cv2.CAP_PROP_FRAME_COUNT)
    video_duration = float(total_frame_count / fps)
    width = video_obj.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = video_obj.get(cv2.CAP_PROP_FRAME_HEIGHT)

    print("reading...: \n\tname:\t\t{} \n\tresolutuion:\t{}x{} \n\tfps:\t\t{} \n\tlenght:\t\t{}sec ({} framse) \n  ".format(video, int(width), int(height), fps, int(video_duration), int(total_frame_count)))

    curr_frame = int(total_frame_count / 2 - N / 2)
    for i in range(curr_frame, curr_frame + N):
        video_obj.set(1, curr_frame)
        ret, frame = video_obj.read()
        time_stamp = round(float(i / fps), 2)
        # cv2.imshow("frame_{}_{}".format(time_stamp, i), frame,)
        print("frame saved:\n\t{}{}_frame_{}.{}".format(dest_path, video_name, time_stamp, frame_ext))
        cv2.imwrite(dest_path + video_name + "_frame_{}.{}".format(time_stamp, frame_ext), frame)
        # curr_frame += i

    print("__________________________\n")
    # # Wait for a keypress
    cv2.waitKey(0)

    # Clean up
    cv2.destroyAllWindows()


if __name__ == '__main__':

    # source_path = 'assets\\'
    # video_name = 'test_video.mp4'
    # dest_path = 'frames_1\\'

    # using argparse for parsing additional arguments
    # parser = ArgumentParser()
    ap = argparse.ArgumentParser(description="Extract N frames from the middle of the video. ")
    ap.add_argument("directory_path", help="specify the directory with the video files.")
    ap.add_argument("-n", "--number_of_frames", required=False, type=int, default=1, help="The number of frames to be extracted.")
    ap.add_argument("-f", "--frame_format", required=False, type=str, default='png', help="The file format of the extracted frame.")
    args = ap.parse_args()

    N = args.number_of_frames
    source_path = args.directory_path + "\\"
    frame_ext = args.frame_format
    # creating 'frames'folder inside the given one
    dest_path = source_path + "frames" + "\\"
    print("\n")
    # print(source_path)
    # print(dest_path)
    try:
        os.mkdir(dest_path)
    except OSError:
        print("There is already such folder: %s \n If you continue some files mey be overwritten! " % dest_path)
        user_input = input('\nDo you want to continue? ')
        if(user_input.lower() == 'n' or user_input.lower() == 'no'):
            print("OK, Bye, bye! ")
            sys.exit()
        else:
            # from termcolor import colored
            # print(colored('*** WARNING! ***', 'yellow'))
            print("*** WARNING! *** \n Files in the folder maight be overwritten!")
    else:
        print("Successfully created the directory %s " % dest_path)

    # listing all video files
    videos = listFiles(source_path)
    # print(source_path + videos[0])
    if(videos):
        for video in videos:
            FrameExtract(source_path + video, dest_path, N, frame_ext)
