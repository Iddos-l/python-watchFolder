# python-watchFolder
Python script that catches events in windows folder



This script uses watchdog to catch an events inside a folder.
It then call ffmpeg  using a shell to convert the event source file to MP4 with custom arguments.


Requirements
    python 2.7, or 3
    watchdog
    runs on Windows


Import watchdog
    pip3 install watchdog
