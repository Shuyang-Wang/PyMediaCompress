import os
import subprocess
from pathlib import Path


# Mac Mini
import os
import subprocess
from pathlib import Path





def downsample(rootdir, desdir,vr='1920' ,pr='2160',overwrite=False):
    Path(desdir).mkdir(parents=True, exist_ok=True)


    n = 0 
    for subdir, dirs, files in os.walk(rootdir):
        print(len(files))
        for file in files:
            n += 1
            print (file)
            if file.lower().endswith('mp4') or file.lower().endswith('mov'):
                if file.startswith('._'):  # Skip Mac filesystem 
                    continue
                if '$RECYCLE.BIN' in subdir: # Skip $RECYCLE.BIN
                    continue

                else:
                    input = subdir + '/' +file
                    output = desdir + input.split(rootdir)[1]
                    Path( desdir+ subdir.split(rootdir)[1]).mkdir(parents=True, exist_ok=True)
                    
                    if (not os.path.isfile(output)) or (overwrite):
                        subprocess.run(['ffmpeg', '-i', input, '-vf', "scale=min'({},iw)':-2".format(vr), '-c:v', 
                        'libx264', '-crf', '20', '-c:a', 'aac', '-map_metadata', '0', output])
                       

            
            if file.lower().endswith('jpg') or file.lower().endswith('jpeg'): ## -------JPEG------
                if file.startswith('._'):  # Skip Mac filesystem 
                    continue
                if '$RECYCLE.BIN' in subdir: # Skip $RECYCLE.BIN
                    continue
                else:
                    input = subdir + '/' +file
                    output = desdir + input.split(rootdir)[1] ## jpeg
                    #output = desdir + (input.split(rootdir)[1]).split('.')[0]+'.heic' ## heic
                    
                    Path( desdir+ subdir.split(rootdir)[1]).mkdir(parents=True, exist_ok=True)
                    
                    if (not os.path.isfile(output)) or (overwrite):
                        subprocess.run(['magick', input,'-resize','{}\>'.format(pr),'-quality', '80', '-auto-orient',output])
                        #subprocess.run(['magick', input,'-resize','{}\>'.format(pr),'-quality', '80', '-auto-orient',output])
                    else:
                        pass

            if file.lower().endswith('NEF') or file.lower().endswith('nef'): ## -------JPEG------
                if file.startswith('._'):  # Skip Mac filesystem 
                    continue
                if '$RECYCLE.BIN' in subdir: # Skip $RECYCLE.BIN
                    continue
                else:
                    input = subdir + '/' +file
                    #output = desdir + input.split(rootdir)[1] ## jpeg
                    output = desdir + (input.split(rootdir)[1]).split('.')[0]+'.jpg' ## jpg
                    
                    Path( desdir+ subdir.split(rootdir)[1]).mkdir(parents=True, exist_ok=True)
                    
                    if (not os.path.isfile(output)) or (overwrite):
                        subprocess.run(['magick', input,'-resize','{}\>'.format(pr),'-quality', '80', '-auto-orient',output])
                        #subprocess.run(['magick', input,'-resize','{}\>'.format(pr),'-quality', '80', '-auto-orient',output])
                    else:
                        pass


# sd card
# sd card
import string
import random

rootdir ='DCIM'
desdir = 'DCIM_downsampled_{}/'.format("".join(random.choice(string.ascii_uppercase) for i in range(5)))
desdir = 'DCIM_downsampled'

downsample(rootdir,desdir,vr='1280', pr='2160', overwrite=False) ## 