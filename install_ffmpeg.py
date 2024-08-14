import os
import shutil
import zipfile
import urllib.request
import subprocess
import time

def download_ffmpeg():
    url = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"
    ffmpeg_zip_path = "ffmpeg-release-essentials.zip"
    ffmpeg_extracted_path = "ffmpeg"

    try:
        # Download ffmpeg zip
        print("Downloading ffmpeg...")
        with urllib.request.urlopen(url) as response:
            with open(ffmpeg_zip_path, 'wb') as out_file:
                shutil.copyfileobj(response, out_file)
        print("Download complete.")

        # Extract ffmpeg zip
        print("Extracting ffmpeg...")
        with zipfile.ZipFile(ffmpeg_zip_path, 'r') as zip_ref:
            zip_ref.extractall(ffmpeg_extracted_path)
        print("Extraction complete.")

        # Find ffmpeg bin directory
        bin_dir = ""
        for root, dirs, files in os.walk(ffmpeg_extracted_path):
            if 'ffmpeg.exe' in files:
                bin_dir = root
                break

        if not bin_dir:
            print("ffmpeg.exe not found.")
            return

        # Add bin directory to PATH
        print(f"Adding ffmpeg to PATH from {bin_dir}...")
        os.environ["PATH"] += os.pathsep + bin_dir

        # Update system PATH
        setx_cmd = f'setx PATH "%PATH%;{bin_dir}"'
        subprocess.run(setx_cmd, shell=True)
        print("ffmpeg successfully added to PATH.")

        # Clean up
        os.remove(ffmpeg_zip_path)
        shutil.rmtree(ffmpeg_extracted_path)
        print("Cleanup complete.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    download_ffmpeg()
