import os
import shutil

folder_path = input("Enter folder path to organize: ").strip()

file_types = {
    "Images": [".jpg",".jpeg",".png",".gif"],
    "Documents": [".pdf",".doc",".docx",".txt"],
    "Videos": [".mp4",".avi",".mkv"],
    "Music": [".mp3",".wav"]
}

for folder in list(file_types)+["Others"]:
    os.makedirs(os.path.join(folder_path,folder),exist_ok=True)

for file in os.listdir(folder_path):
    src=os.path.join(folder_path,file)
    if os.path.isfile(src):
        ext=os.path.splitext(file)[1].lower()
        moved=False
        for folder,exts in file_types.items():
            if ext in exts:
                shutil.move(src,os.path.join(folder_path,folder,file))
                print(f"Moved {file} -> {folder}")
                moved=True
                break
        if not moved:
            shutil.move(src,os.path.join(folder_path,"Others",file))
            print(f"Moved {file} -> Others")
print("Done!")
