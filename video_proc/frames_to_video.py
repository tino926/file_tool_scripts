import os
import glob
import subprocess

# Define the directory containing the JPEG images
IMGDIR = 'D:\\Download\\abc'

# Define the output video file name
OUTVID = 'D:\\Download\\abc.mp4'

# Define the frames per second (FPS)
FPS = 15

# Step 1: List all JPEG files in the specified directory
jpeg_files = glob.glob(f'{IMGDIR}/*.jpg')

# Ensure the files are sorted in the correct order
jpeg_files.sort()

# Step 2: Create a temporary text file for the concat demuxer
concat_file = f'{OUTVID}.txt'
with open(concat_file, 'w') as f:
    for file in jpeg_files:
        f.write(f"file '{file}'\n")

# Step 3: Construct the command
# Start with the base command and the input files
command = ['ffmpeg',
           '-f', 'concat',
           '-safe', '0',  # Allow file paths in the concat list file
           '-i', concat_file,
           '-r', str(FPS),
           '-c:v', 'libx264',  # Use the libx264 codec for video encoding
           # Pad the video to ensure dimensions are even
           '-vf', 'pad=ceil(iw/2)*2:ceil(ih/2)*2',
           '-pix_fmt', 'yuv420p',
           OUTVID]

# Step 4: Execute the command
subprocess.run(command)

# Step 5: Clean up the temporary text file
os.remove(concat_file)
