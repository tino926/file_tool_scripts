import os
import subprocess

# Get the current working directory
current_dir = os.getcwd()

# List of video file extensions to process
video_extensions = ['.mp4', '.avi', '.mkv']

# Iterate over all files in the current directory
for filename in os.listdir(current_dir):
    # Check if the file has one of the video extensions
    if any(filename.endswith(ext) for ext in video_extensions):
        # Extract the base name without the extension
        base_name = os.path.splitext(filename)[0]
        # Create a new directory with the base name
        new_dir = os.path.join(current_dir, base_name)
        os.makedirs(new_dir, exist_ok=True)
        # Construct the ffmpeg command
        ffmpeg_cmd = [
            'ffmpeg', '-i', filename, '-q:v', '1', '-fps_mode', 'passthrough', '-frame_pts', '1',
            os.path.join(new_dir, '%%08d.jpg')
        ]
        # Execute the ffmpeg command
        subprocess.run(ffmpeg_cmd, check=True)
        