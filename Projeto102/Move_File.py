import os
import shutil

from_dir = "C:/Users/Gabriel Martins/Downloads/"
to_dir = "C:/Users/Gabriel Martins/Arquivos_Documentos/ZIPs/"

list_of_files = os.listdir(from_dir)

for file in list_of_files:
    name,extension=os.path.splitext(file)

    if(extension == ""):
        continue
    elif(extension in [".zip"]):
        path1=from_dir+file
        path2=to_dir
        path3=to_dir+file
        if(os.path.exists(path2)):
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            shutil.move(path1,path3)