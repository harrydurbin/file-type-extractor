
import shutil
import os

basepath = r'C:\Users\Harrison\Desktop\takeout-20170302T063057Z-001\Takeout\Google_Photos'

ctr=0
os.chdir(basepath)
for fname in os.listdir(basepath):
    path = os.path.join(basepath, fname)
    if os.path.isdir(path):
        # print  path
        for f in os.listdir(path):
            # print f
            if (f.endswith(".jpg")) or (f.endswith(".JPG")) or (f.endswith(".png")) or (f.endswith(".PNG")) or (f.endswith(".mp4")) or (f.endswith(".gif")):

                ff = os.path.join(path, f)
                shutil.copy(ff, basepath)
                ctr +=1
#               print 'moved ', f
print ctr , 'files were moved.'

