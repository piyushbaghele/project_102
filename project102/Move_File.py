import os
import shutil

from_dir = "C:/Users/punam/Downloads"

to_dir = "C:/Users/punam/Desktop/class102"

list_of_files = os.listdir(from_dir)
#print(list_of_files)

for x in list_of_files:
    root,ext = os.path.splitext(x)
    # print(root)
    # print(ext)

    if ext=="":
        continue
    if ext in[".doc",".txt",".doxc",".pdf"]:
        path1 = from_dir + "/" + x
        path2 = to_dir + "/" + "document_files"
        path3 =  to_dir + "/"+ "document_files" + "/" + x
        print(path1)
        print(path3)
        
        if os.path.exists(path2):
            print("The file is moving")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("The file is moving")
            shutil.move(path1,path3)
            