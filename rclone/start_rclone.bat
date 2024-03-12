set rcfdr=d:\greenware\rclone ; folder of the rclone execution file
set mfdr=d:\z_rc              ; root folder to mount network drives
set uname=user                ; webui username
set upass=pass                ; webui password
set prefixFilter=ppp          ; remote name starting with this will not be mounted


cd /d %rcfdr%
rclone selfupdate

start "rc_web" /min cmd /c "rclone rcd -v --rc-web-gui --rc-web-gui-no-open-browser --rc-web-gui-update --rc-user %uname% --rc-pass %upass%"
timeout 5


@ECHO off
setlocal EnableDelayedExpansion
set LF=^


REM !!! The upper two empty lines are required here
set "output="
for /F "delims=" %%f in ('rclone listremotes --long') do (
    if defined output set "output=!output!!LF!"

    :: if the remote name not start with prefixFilter, add it to list
    set tmpstr=%%f
    :: remove space
    SET "tmpstr_=!tmpstr: =% & rem.%!"
    if NOT "!tmpstr:~0,3!"=="!prefixFilter!" set "output=!output!!tmpstr_!"
)

echo !output! > %mfdr%\log.txt
REM timeout 15
REM exit 0


set "set1=pcloud"

for %%f in (!output!) do (
    set tmpstr=%%f
	for /F "tokens=1 delims=:" %%g in ("!tmpstr!") do set "name=%%g"
	set remo=!name!:

	set devi=!tmpstr:*:=!

    rem echo -------------
    echo "!tmpstr! => !remo! => !devi! => !name!"
    rem echo "onedrive pcloud"| findstr /i "\<!devi!\>" >nul && echo yes || echo no

    set "found=0"
    for %%S in (!set1!) do (
        if "!found!"=="0" if "!devi!"=="%%S" (
            ::echo yes
            set "found=1"
            rclone rc mount/mount --rc-user %uname% --rc-pass %upass% ^
                vfsOpt={\"CacheMode\":3} fs=!remo! mountPoint=%mfdr%\!name! 
        )
    )
    if "!found!"=="0" (
        ::echo no
        rclone rc mount/mount --rc-user %uname% --rc-pass %upass% ^
            vfsOpt={\"CacheMode\":3} fs=!remo! mountPoint=%mfdr%\!name! 
    )

)

timeout 15
exit 0

