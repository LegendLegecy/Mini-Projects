from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
# Authenticate and create the PyDrive client
gauth = GoogleAuth()
gauth.DEFAULT_SETTINGS['client_config_backend'] = 'settings'
gauth.DEFAULT_SETTINGS['client_config_file'] = 'settings.yaml'
gauth.LocalWebserverAuth()  # Creates local webserver and auto handles authentication
drive = GoogleDrive(gauth)

# Google Drive folder ID where files will be uploaded
PARENT_FOLDER_ID = "12CwwTZ-jJSMDhtEDMYg7VQw3Edf3PfYX"

# Excluded file extensions and directory names
EXCLUDED_EXTENSIONS = {".exe", ".spec"}
EXCLUDED_DIRECTORIES = {"dist", "built"}

def upload_to_drive(parent_folder_id, local_path):
    """
    Recursively uploads files and folders to Google Drive.
    """
    for item in os.listdir(local_path):
        item_path = os.path.join(local_path, item)

        # Skip excluded directories
        if os.path.isdir(item_path) and item in EXCLUDED_DIRECTORIES:
            continue

        # Skip excluded file extensions
        if os.path.isfile(item_path) and any(item.endswith(ext) for ext in EXCLUDED_EXTENSIONS):
            continue

        if os.path.isdir(item_path):
            # Create a folder in Google Drive
            folder_metadata = {
                "title": item,
                "parents": [{"id": parent_folder_id}],
                "mimeType": "application/vnd.google-apps.folder"
            }
            folder = drive.CreateFile(folder_metadata)
            folder.Upload()
            print(f"Created folder: {item}")

            # Recursively upload the contents of the folder
            upload_to_drive(folder["id"], item_path)
        else:
            # Upload a file to Google Drive
            file = drive.CreateFile({
                "title": item,
                "parents": [{"id": parent_folder_id}]
            })
            file.SetContentFile(item_path)
            file.Upload()
            print(f"Uploaded file: {item}")

if __name__ == "__main__":
    # Start uploading from the current directory
    current_directory = os.getcwd()
    upload_to_drive(PARENT_FOLDER_ID, current_directory)