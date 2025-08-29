import os
import shutil
def organize_folder(folder_path):
    file_types={
        'images':['.jpg','.jpeg','.png','.gif'],
        'Document':['.pdf','.docx','.txt','.xlsx'],
        'Videos':['.mp4','.avi','.mkv'],
        'Audio':['.mp3','.wav'],
        'Archives':['.zip','.rar'],
        'Scripts':['.py','.js']
    }
    for filename in os.listdir(folder_path):
        file_path=os.path.join(folder_path,filename)
        if os.path.isfile(file_path):
            ext=os.path.splitext(filename)[1]
            for folder,extension in file_types.items():
                if ext.lower() in extension:
                    target_folder=os.path.join(folder_path,folder)
                    os.makedirs(target_folder,exist_ok=True)
                    shutil.move(file_path,os.path.join(target_folder,filename))
                    break
path=input("Enter the path of file: ")
organize_folder(path)
