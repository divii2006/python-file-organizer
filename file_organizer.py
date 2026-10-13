import os
import shutil

def organize_files(folder_path):
    if not os.path.isdir(folder_path):
        print("Error: Folder does not exist.")
        return

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if not os.path.isfile(file_path):
            continue

        extension = os.path.splitext(filename)[1].lower()
        folder_name = extension[1:] if extension else "no_extension"

        destination_folder = os.path.join(folder_path, folder_name)
        os.makedirs(destination_folder, exist_ok=True)

        destination_path = os.path.join(destination_folder, filename)

        if os.path.exists(destination_path):
            print(f"Skipped: {filename}")
            continue

        shutil.move(file_path, destination_path)
        print(f"Moved: {filename} -> {folder_name}/")

    print("File organization completed!")

if __name__ == "__main__":
    target_folder = input("Enter the folder path to organize: ")
    organize_files(target_folder)