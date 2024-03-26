# Video Processing Scripts

This repository contains Python scripts and a batch file designed for processing 
video files. The scripts are capable of extracting frames from videos, embedding 
subtitles into video files, and automating the frame extraction process.

## Table of Contents

- [Video Processing Scripts](#video-processing-scripts)
  - [Table of Contents](#table-of-contents)
  - [Scripts Overview](#scripts-overview)
    - [extract\_frames\_1fps](#extract_frames_1fps)
      - [Usage](#usage)
    - [deal\_video.py](#deal_videopy)
      - [Usage](#usage-1)
    - [frames\_to\_video.py](#frames_to_videopy)
      - [Features](#features)
      - [Usage](#usage-2)
  - [Configuration](#configuration)
  - [Contributing](#contributing)

## Scripts Overview

### extract_frames_1fps

This script extracts frames from videos, with two versions available: a Windows 
batch file and a Python script.

#### Usage

1. Place the `extract_frames_1fps.bat` or `extract_frames_1fps.py` file in the 
   directory containing the video files you want to process.
2. Run the batch file by double-clicking it or executing it from the command 
   line.

### deal_video.py

This Python script automates the embedding of subtitles into video files using 
FFmpeg. It is designed for batch processing of multiple video files with their 
corresponding subtitle files, simplifying the process of adding subtitles to 
video content.

#### Usage

1. Ensure you have Python installed on your system.
2. Install the required Python packages by running 
   `pip install ffmpeg-python configparser`.
3. Place the `deal_video.py` file in the directory containing the video files 
   and their corresponding subtitle files.
4. Run the script by executing `python deal_video.py` from the command line.

### frames_to_video.py

This Python script converts a series of JPEG images into a video file. It's 
particularly useful for creating videos from a sequence of frames, such as those 
extracted from a video file. The script uses FFmpeg for the conversion process, 
ensuring high-quality video output.

#### Features

- Automatically sorts JPEG files in the specified directory to ensure the 
  correct order of frames.
- Constructs a temporary text file for the FFmpeg concat demuxer, which is used 
  to concatenate the frames into a video.
- Allows customization of the output video's frames per second (FPS) and 
  resolution.
- Cleans up the temporary text file after the video has been created.

#### Usage

1. Ensure you have Python installed on your system.
2. Install the required Python packages by running `pip install ffmpeg-python`.
3. Modify the `IMGDIR` variable in the script to point to the directory 
   containing your JPEG images.
4. Optionally, adjust the `FPS` variable to change the video's frames per second.
5. Run the script by executing `python frames_to_video.py` from the command line.

## Configuration

Both `extract_frames_1fps.py` and `deal_video.py` scripts support configuration 
through a `settings.ini` file located in a `./pri` directory. The `settings.ini` 
file should contain the necessary settings for the scripts to function correctly. 
See the script documentation for details on the required settings.

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.
