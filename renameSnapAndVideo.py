import os, sys
import argparse
import shutil

### global variables for storing file names
snap_count = 0      #count renamed snapshots
snap_file_names = []

raw_count = 0      #count renamed raws
raw_file_names = []

yuv_count = 0      #count renamed yuvs
yuv_file_names = []

video_count = 0      #count renamed video
video_file_names = []

### checks if the given directory exists, if not - prints an error
def is_existing_directory(directory_path):
    if not os.path.exists(directory_path):
        print("(>_<)  Oops! No such directory (-_-)  \n")
        return

### lists all jpg, raw, yuv and video files and stores the names in global variables
def listing_files_for_renaming(directory_path):

    is_existing_directory(directory_path)    

    for file_name in os.listdir(directory_path):
        if (file_name.endswith(".jpg") or file_name.endswith(".JPG") or  file_name.endswith(".jpeg")):
            snap_file_names.append(file_name)
        if (file_name.endswith(".raw") or file_name.endswith(".RAW") ):
            raw_file_names.append(file_name)
        if (file_name.endswith(".yuv") or file_name.endswith(".YUV") ):
            yuv_file_names.append(file_name)
        if (file_name.endswith(".mp4") or file_name.endswith(".MOV") ):
            video_file_names.append(file_name)
    
    if(len(snap_file_names) > 0 or len(raw_file_names)> 0 or len(video_file_names)> 0):
        print("Hooray! There are some files for renaming.")
        print("\n*************************** >^_^< ***************************\n")

### Copies files to the outside directory and renames them with the name of the current directory    
def copy_rename_from_subfolders(file_names, root_abs_directory, directory_name):
    if not file_names:
        return
    print("============")
    # print(root_abs_directory)
    # print(directory_name)

    files_count = len(file_names)
    k = 0 
    renamed_count = 0; 
    for k in range(files_count):
        file_name = file_names[0]
        new_file_name = directory_name+"_"+file_name
        print("{}: {} = {}".format(k, file_name, new_file_name))
        
        shutil.copy(os.path.join(root_abs_directory, directory_name, file_name), root_abs_directory)
        os.rename(os.path.join(root_abs_directory,file_name), os.path.join(root_abs_directory,new_file_name))

        file_names.pop(0)
        renamed_count += 1

    print(" ")
    return renamed_count
 
### test type where each test case is in different folder
### this method copies the files from each subfilfder and adds the name of the folder as a prefix of the original file name
def rename_in_subfolders(directory_path):
    
    is_existing_directory(directory_path)    

    for dir_name in os.listdir(directory_path):
        print(" - " + os.path.join(directory_path,dir_name))
        listing_files_for_renaming(os.path.join(directory_path, dir_name)) 
        
        snap_count = copy_rename_from_subfolders(snap_file_names, directory_path, dir_name)
        raw_count = copy_rename_from_subfolders(raw_file_names, directory_path, dir_name)
        yuv_count = copy_rename_from_subfolders(yuv_file_names, directory_path, dir_name)
        video_count = copy_rename_from_subfolders(video_file_names, directory_path, dir_name)
    
        ###
        if((snap_count != 0) or (video_count != 0) or (raw_count != 0)):
            print(str(snap_count) + " snapshots are renamed from all subfolders")
            print(str(raw_count) + " raws are renamed")
            print(str(yuv_count) + " yuvs are renamed")
            print(str(video_count) + " videos are renamed")
            print("\n*************************** \(^o^)/ ***************************\n")


    
def renameMultipleCameras(file_names, directory, dir, start_idx, count):
    n = len(file_names)
    st_idx = int(start_idx) - 1
    renamedCount = 0; 
    
    for k in range(st_idx, st_idx+n):
        #print(k)
        for p in range(0,3*count):
            if(len(file_names)>0 ):
                file_name = file_names[0]
                pref = file_name.split("_")
                oldName = file_name.split(".")
                timestamp = oldName[0].split("_")
                if(p >= 0 and p <count):
                    prefix = "case" + str(k+1) + "_W" +"_" + dir 
                if(p >= count and p <(2*count)):
                    prefix = "case" + str(k+1)  + "_UW" +"_" + dir
                if(p >= (2*count) and p <=(3*count)):
                    prefix = "case" + str(k+1) + "_T" +"_" + dir  
                newName = oldName[0].replace(pref[0], prefix, 1) + "." + oldName[1]
                print("- "+file_name+ " = " + newName)
                os.rename(directory+file_name, directory+newName)
                file_names.pop(0)
                renamedCount = renamedCount+1
        print('')
        if(renamedCount >= n):
            break
    print(" ")
    return renamedCount

def renameSingleCamera(file_names, directory, dir, start_idx, count):
    n = len(file_names)
    st_idx = int(start_idx) - 1
    renamedCount = 0; 
    for k in range(st_idx, st_idx+n):
        for p in range(0,count):
            if(len(file_names)>0):
                file_name = file_names[0]
                pref = file_name.split("_")
                oldName = file_name.split(".")
                timestamp = oldName[0].split("_")
                prefix = "case" + str(k+1) +"_" + dir
                newName = oldName[0].replace(pref[0], prefix, 1) + "." + oldName[1]
                print("- "+file_name+ " = " + newName)
                os.rename(directory+file_name, directory+newName)
                file_names.pop(0)
                renamedCount = renamedCount+1
        print('')
        if(renamedCount >= n):
            break
    print(" ")
    return renamedCount

def renameInitialSingle(file_names, directory, dir):   
    n = len(file_names)
    st_idx = 0 
    renamedCount = 0; 
    for k in range(st_idx, st_idx+n):
        if(len(file_names)>0):
            file_name = file_names[0]
            pref = file_name.split("_")
            oldName = file_name.split(".")
            timestamp = oldName[0].split("_")
            prefix = dir
            newName = oldName[0].replace(pref[0], prefix, 1) + "." + oldName[1]
            print("- "+file_name+ " = " + newName)
            os.rename(directory+"\\"+file_name, directory+"\\"+newName)
            file_names.pop(0)
            renamedCount = renamedCount+1
        print('')
        if(renamedCount >= n):
            break
    print(" ")
    return renamedCount



def renameBasedOnTestType(directory, dir, start_idx, count, testType):
    if (testType == 3):
        video_count = renameMultipleCameras(video_file_names,directory, dir, start_idx,1)
        snap_count = renameMultipleCameras(snap_file_names, directory, dir, start_idx,count)
        raw_count = renameMultipleCameras(raw_file_names, directory, dir, start_idx,count)  
        # print("testType=3")
    elif (testType == 2):
        snap_count = renameSingleCamera(snap_file_names, directory, dir, start_idx,count)
        raw_count = renameSingleCamera(raw_file_names, directory, dir, start_idx,count)  
        video_count = renameSingleCamera(video_file_names, directory, dir, start_idx,1)
        # print("testType=2")
    elif (testType == 1):
        snap_count = renameInitialSingle(snap_file_names, directory, dir)
        raw_count = renameInitialSingle(raw_file_names, directory, dir)  
        video_count = renameInitialSingle(video_file_names, directory, dir)
        # print("testType=1")

def renameTestImages(directory, dir, start_idx, count, testType):
    
    ### check for subfolders \\ a.k.a if there is testing from multiple devices
    list_subfolders_with_paths = [f.path for f in os.scandir(directory) if f.is_dir()]
    
    if(len(list_subfolders_with_paths) == 0):        
        listFilesForRenaming(directory)
        renameBasedOnTestType(directory, dir, start_idx, count, testType)
            
    elif(len(list_subfolders_with_paths) > 0):
        for directory in list_subfolders_with_paths:     
            dir = get_dir_name(directory)
            listFilesForRenaming(directory)  
            renameBasedOnTestType(directory+"\\", dir, start_idx, count, testType)        

        
        
    if((snap_count != 0) or (video_count != 0) or (raw_count != 0)):
        print(str(snap_count) + " snapshots are renamed")
        print(str(raw_count) + " raws are renamed")
        print(str(video_count) + " videos are renamed")
        print("\n*************************** \(^o^)/ ***************************\n")

def get_dir_name(dir_path):
    directory = dir_path.split(os.path.sep)
    dir_name = directory[-1]   
    return dir_name
    
if __name__ == '__main__':

### using argparse for parsing additional arguments

    ap = argparse.ArgumentParser(description="Rename the snapshots, raw files and videos in the given folder.\n Each number of _count files will be renamed in the form of: case#_directoryName_originalTimeStamp.*** \n\n\n In case of renaming files from tree sensors the first _count of files will have the letter W for 'wide camera', next _count of files will have the letters UW for 'Ultra Wide camera, the next _count of files will be with the letter T for 'Tele camera' \n example: case#_directoryName_UW_originalTimeStamp.***.")
    ap.add_argument("image_directory_path", help="specify the directory with the files for renaming.")
    ap.add_argument("-i", "--start_idx", required=False,type=int, default=1, 
help="Start index for enumarating the test cases. The default value is 1.")
    ap.add_argument("-c", "--count", required=False, type=int, default=3, 
help="The number of shots per test case. The default value is 3.")
    ap.add_argument("-t", "--test_type", required=True, default=2, type=int, 
help="""Choose the type of testing for renaming: 
                                    0-Initial (Each test case is in differernt SUB-folder.); 
                                    1-Initial single (doesnt rename the subfolders); 
                                    2-Subjective testing from single camera; 
                                    3-Subjective testing triple camera; default value=2""" )
    args = ap.parse_args()
    
    image_directory_path = args.image_directory_path
    directory_name = get_dir_name(image_directory_path)
    print("\n")
    # print(image_directory_path)
    # print(directory_name)
    
    if args.start_idx is not None:
        start_idx = args.start_idx
        #print(args.start_idx)
    else:
        start_idx = 1
        
    if args.count is not None:
        count = args.count
    else:
        count = 3
    
    if args.test_type is not None:
        test_type = args.test_type
    
    if test_type == 0:
        rename_in_subfolders(image_directory_path)
    else:    
        renameTestImages(image_directory_path+"\\", directoryName, start_idx, count, testType)
