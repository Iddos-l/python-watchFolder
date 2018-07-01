# python-watchFolder
Python script that catches events in windows folder



This script uses watchdog to catch events in a folder.
It then calls ffmpeg  using a shell to convert the event source file to MP4 with custom arguments.


Requirements.
- python 3 / 2.7
- watchdog
- runs on Windows


Import watchdog.
- pip3 install watchdog

Known bug.
 - Fast read render will not work
