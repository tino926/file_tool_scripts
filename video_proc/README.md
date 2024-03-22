# Video Processing Scripts

This repository contains three Python scripts and a batch file designed for 
processing video files. The scripts are designed to extract frames from video 
files, embed subtitles into video files, and a batch file to automate the frame 
extraction process.

## Contents

- [Video Processing Scripts](#video-processing-scripts)
  - [Contents](#contents)
  - [extract\_frames\_1fps.bat](#extract_frames_1fpsbat)
    - [Usage](#usage)
  - [extract\_frames\_1fps.py](#extract_frames_1fpspy)
    - [Usage](#usage-1)
  - [deal\_video.py](#deal_videopy)
    - [Usage](#usage-2)
  - [Configuration](#configuration)
  - [Contributing](#contributing)

## extract_frames_1fps.bat

This batch script extracts frames from video files in the current folder. It 
processes all `.mp4`, `.avi`, and `.mkv` files in the current directory, 
creating a new folder for each video file named after the video file itself. The 
frames are extracted at 1 frame per second (1fps) using FFmpeg.

### Usage

1. Place the `extract_frames_1fps.bat` file in the directory containing the 
   video files you want to process.
2. Run the batch file by double-clicking it or executing it from the command 
   line.

## extract_frames_1fps.py

This Python script is a more advanced version of the batch script, offering 
similar functionality but with additional features such as configuration through 
an `settings.ini` file. It extracts frames from video files located in a 
specified directory, creating a new directory for each video file named after 
the video file itself.

### Usage

1. Ensure you have Python installed on your system.
2. Install the required Python packages by running 
   `pip install ffmpeg-python configparser`.
3. Place the `extract_frames_1fps.py` file in the directory containing the video 
   files you want to process.
4. Run the script by executing `python extract_frames_1fps.py` from the command 
   line.

## deal_video.py

This Python script automates the embedding of subtitles into video files using 
FFmpeg. It is designed for batch processing of multiple video files with their 
corresponding subtitle files, simplifying the process of adding subtitles to 
video content. The script defines the paths to the video file and the directory 
containing subtitle files, constructs an FFmpeg command to embed each subtitle 
stream into the video file, and executes the command to process the video.

### Usage

1. Ensure you have Python installed on your system.
2. Install the required Python packages by running 
   `pip install ffmpeg-python configparser`.
3. Place the `deal_video.py` file in the directory containing the video files 
   and their corresponding subtitle files.
4. Run the script by executing `python deal_video.py` from the command line.

## Configuration

Both `extract_frames_1fps.py` and `deal_video.py` scripts support configuration 
through an `settings.ini` file located in a `./pri` directory. 
The `settings.ini` file should contain the necessary settings for the scripts to 
function correctly. See the script documentation for details on the required 
settings.

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.
