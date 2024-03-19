@echo off
setlocal enabledelayedexpansion

for %%f in (*.mp4 *.avi *.mkv) do (
    set "filename=%%~nf"
    mkdir "!filename!"
    ffmpeg -i "%%f" -q:v 1 -fps_mode passthrough -frame_pts 1 "!filename!/%%08d.jpg"
)

endlocal