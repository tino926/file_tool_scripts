import os
import configparser
import ffmpeg

# Check if the ./pri directory exists and contains settings.ini
if os.path.exists('./pri'):
    # Use configparser to read the settings
    config = configparser.ConfigParser()
    config.read('./pri/setting.ini')
    video_dir = config.get('EXTRACT_FRAMES', 'video_fdr')
else:
    # Get the current working directory
    video_dir = os.getcwd()


# List of video file extensions to process
video_extensions = ['.mp4', '.avi', '.mkv']

# Iterate over all files in the current directory
for filename in os.listdir(video_dir):
    # Check if the file has one of the video extensions
    if any(filename.endswith(ext) for ext in video_extensions):
        # Extract the base name without the extension
        base_name = os.path.splitext(filename)[0]
        # Create a new directory with the base name
        new_dir = os.path.join(video_dir, base_name)
        os.makedirs(new_dir, exist_ok=True)

        # Construct the ffmpeg command
        stream = ffmpeg.input(os.path.join(video_dir, filename))
        stream = ffmpeg.output(stream, new_dir+'/%08d.jpg', q=1, 
                               fps_mode='passthrough', 
                               frame_pts=1)
        ffmpeg.run(stream)
