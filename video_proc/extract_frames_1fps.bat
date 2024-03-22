:: This batch script extracts frames from video files in current folder
:: It processes all .mp4, .avi, and .mkv files in the current directory, 
:: creating a new folder for each video file named after the video file itself.


@echo off
setlocal enabledelayedexpansion

for %%f in (*.mp4 *.avi *.mkv) do (
    set "filename=%%~nf"
    mkdir "!filename!"
    ffmpeg -i "%%f" -q:v 1 -fps_mode passthrough -frame_pts 1 "!filename!/%%08d.jpg"
)

endlocal