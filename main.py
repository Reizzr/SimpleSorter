import os
from pathlib import Path
import shutil

files = os.listdir(path='.')

##################################
##           Настройка          ##
##################################

images = ["jpg", "jpeg", "png", "gif", "bmp", "svg", "webp", "tiff", "heic"]
audio = ["mp3", "wav", "flac", "aac", "ogg", "m4a", "wma"]
videos = ["mp4", "mov", "avi", "mkv", "flv", "webm", "wmv", "mpeg"]
documents = ["pdf", "doc", "docx", "xls", "xlsx", "ppt", "pptx", "txt", "rtf"]
archives = ["zip", "rar", "7z", "tar", "gz", "iso"]
programs = ["exe", "msi", "dmg", "pkg", "deb", "apk"]
scripts = ["py", "js", "php", "sh", "bat", "ps1", "cpp", "h", "java"]
torrents = ["torrent"]
design = ["psd", "ai", "fig", "xd", "sketch"]
database = ["sql", "db", "sqlite", "csv", "json"]
models = ["stl", "obj", "fbx", "blend", "3ds"]



def main():
    mode = int(input("""Выберите режим сортировки:\n
    1 - Типы файлов\n
    2 - Расширения файлов\n
Ваш выбор [По умолчанию 1]: """))
    
    copy = int(input("""Копировать или переносить файлы?:\n
    1 - Копировать\n
    2 - Переносить\n
Ваш выбор [По умолчанию 1]: """))
    

    #os.makedirs("sorter", exist_ok=True)
    dir = "sorter/"
    current_file = os.path.basename(__file__)  # Например: "script.py"
    for file in files:
            if "." in file and file != current_file:
                extension = file.split(".")[-1]
                if mode==2:
                    target_dir = dir + "." + extension
                else:
                    if extension in images:
                        target_dir = dir + "images"
                    elif extension in audio:
                        target_dir = dir + "audio"
                    elif extension in videos:
                        target_dir = dir + "videos"
                    elif extension in documents:
                        target_dir = dir + "documents"
                    elif extension in archives:
                        target_dir = dir + "archives"
                    elif extension in programs:
                        target_dir = dir + "programs"
                    elif extension in scripts:
                        target_dir = dir + "scripts"
                    elif extension in torrents:
                        target_dir = dir + "torrents"
                    elif extension in design:
                        target_dir = dir + "design"
                    elif extension in database:
                        target_dir = dir + "database"
                    elif extension in models:
                        target_dir = dir + "models"              
                    else:
                        target_dir = dir + "other"
                os.makedirs(target_dir, exist_ok=True)
                if copy == 2:
                    shutil.move(file, target_dir)
                else:
                    shutil.copy2(file, target_dir)

    

if __name__ == "__main__":
    main()
    input()
