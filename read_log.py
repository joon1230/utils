import os
import shutil

f_path = "D:/VIDEO/car/RESULTS/F20004_3"
load_path = os.path.join( f_path , "load" )
xml_lst = sorted(os.listdir( os.path.join( f_path , 'xml') ))
video_lst = sorted(os.listdir( os.path.join( f_path , 'video' )))

def make_dir( path ):
    try:
        os.mkdir( path )
    except:
        pass
#
for idx in range(len(xml_lst)):
    xml,video = xml_lst[idx], video_lst[idx]
    dir_name = xml[:-4]
    destination_path = os.path.join( load_path, dir_name)
    make_dir(destination_path)

    origin_xml, origin_video = os.path.join( f_path, "xml", xml ), os.path.join( f_path, "video", video )
    shutil.copyfile( origin_xml, os.path.join(destination_path, xml) )
    shutil.copyfile( origin_video, os.path.join(destination_path, video))
#

print(os.path.join( f_path , video_lst[2] , xml_lst[0] ))



