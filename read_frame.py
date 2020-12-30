import xml.etree.ElementTree as ET
import pandas as pd
import os


DIRECTORY_PATH = "D:/VIDEO/car/RESULTS/F20010_3/xml"
df = []


def get_image_counts( root ):
    return int(root.findall('image')[-1].attrib['id']) + 1

def get_box_counts( root ):
    cnt = 0
    for b in root.iter('box'):
        if b.tag == 'box':
            cnt += 1
    return cnt


file_list = [f for f in os.listdir(DIRECTORY_PATH) if '.xml' in f]
for file in file_list:
    xml = open( os.path.join( DIRECTORY_PATH , file ), 'rt', encoding='utf-8' )
    parser = ET.parse(xml)
    root = parser.getroot()
    df.append([file[:-4] , get_box_counts( root ), get_image_counts( root )])

res = pd.DataFrame( df, columns = ['video_id', 'box_cnts', 'image_cnts'] )
res.to_csv(os.path.join( DIRECTORY_PATH , 'total_counts.csv') , encoding= 'utf-8' , index = False)

