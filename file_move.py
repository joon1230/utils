import os
import shutil


current_path = input("move_file_lst : ")
file_lst_path = input("file_lst.txt : ")


#%%

file_lst = open(file_lst_path).read().split("\n")
print( file_lst )
def copy_files( file_type ):
    global current_path, file_lst, save_path
    try:
        os.mkdir(os.path.join(current_path,"results") )
    except:
        pass
    save_path = os.path.join(current_path, "results")

    for file in file_lst:
        file = file + file_type
        shutil.copyfile( os.path.join(current_path, file ) , os.path.join(save_path, file) )
copy_files( ".avi")
""" 
for f_l in file_lst:
    f_l = f_l.split(",")
    file_name = f_l[0]
    date = file_name[9:-4]
    shutil.copyfile( os.path.join( current_path, date, file_name+".avi" ), os.path.join(save_path, file_name+".avi") )
"""