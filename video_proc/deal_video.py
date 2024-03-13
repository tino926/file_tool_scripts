"""
This script automates the embedding of subtitles into video files using FFmpeg. 
It is designed for batch processing of multiple video files with their 
corresponding subtitle files, simplifying the process of adding subtitles to 
video content. The script defines the paths to the video file and the directory 
containing subtitle files, constructs an FFmpeg command to embed each subtitle 
stream into the video file, and executes the command to process the video.
"""

import subprocess
import os
import configparser


# Check if the ./pri/ subfolder exists
if os.path.exists('./pri/'):
    # Read the setting.ini file
    config = configparser.ConfigParser()
    config.read('./pri/setting.ini')

    VIDEO = config.get('Settings', 'video_path')
    SUBTITLES_DIR = config.get('Settings', 'sub_fdr')
else:
    # Default paths if the subfolder does not exist
    VIDEO = "D:/a.mkv"
    SUBTITLES_DIR = 'D:/a'


# Get the directory of the video file
VIDEO_DIR = os.path.dirname(VIDEO)
# Define the output directory for the processed video
OUTPUT_DIR = os.path.join(VIDEO_DIR, 'out')

# Function to embed subtitles into a video file
def embed_subtitles(video_path, subtitles):
    # Initialize the command list for ffmpeg
    cmd = ['ffmpeg', '-i', video_path]

    # Loop through each subtitle file
    for i, subtitle in enumerate(subtitles, start=1):
        # Add the subtitle file to the command
        cmd.extend(['-i', subtitle])
        # Map the subtitle stream to the output
        cmd.append('-map')
        cmd.append(str(i))
        # Specify the codec for the subtitle stream
        cmd.append('-c:s:{}'.format(i-1))
        # cmd.append('mov_text')

    # Copy all streams to the output file
    cmd.append('-c copy output.mkv')

    subprocess.run(cmd)

# Get a list of valid subtitle files in the subtitle directory
sub_list = [f for f in os.listdir(SUBTITLES_DIR) if f.endswith(
    ('.vtt', '.srt', '.ssa', '.dfxp', '.sub'))]

# Call the function to embed subtitles into the video
embed_subtitles(VIDEO, [os.path.join(SUBTITLES_DIR, f) for f in sub_list])
