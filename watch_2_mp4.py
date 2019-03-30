#!/usr/bin/env python3
import os, time
from subprocess import call
from tkinter import Tk, filedialog
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

# User set watch and output folders
Tk().withdraw()
watchFolder = filedialog.askdirectory(title='Choose watch folder')
if not watchFolder:     # In case user select "Cancel"
    exit(-1)
outputFolder = filedialog.askdirectory(title='Choose output folder')
if not outputFolder:
    exit(-1)

# Creating an event handler class to catch events
class MyHandler(PatternMatchingEventHandler):

    doneList = []   # Converted files will be added here

    def add_to_doneList(self, item):
        """Returns true if event file is already in the doneList. if not will add it"""
        if item in MyHandler.doneList:
            return True
        else:
            MyHandler.doneList.append(item)
            return False

    def convert(self, filePath, outputFolder):
        """ Adds engine(ffmpeg) to path and calls it with args """
        split = os.path.splitext(filePath)[0]
        fileName = os.path.basename(split)
        outputPath = '{}\\{}.mp4'.format(outputFolder, fileName)

        call(['set', 'PATH=C:\\Id_Convert\\engine\\bin;%PATH%', '&&',
             'ffmpeg', '-i', filePath, '-c:v', 'libx264',
             '-pix_fmt', 'yuv420p', '-profile:v', 'high', '-crf', '15', '-y', outputPath], shell=True)

    def on_created(self, event):
        """Waits for event to be ready (Not changing in size)
           Then adding to done list and calling convert"""
        time.sleep(1)
        try:
            fileSizeBefore = os.path.getsize(event.src_path)
            while(1):
                time.sleep(4)
                fileSizeAfter = os.path.getsize(event.src_path)
                if fileSizeAfter == fileSizeBefore:
                    break
                else:
                    fileSizeBefore = fileSizeAfter

            if not self.add_to_doneList(event):
                self.convert(event.src_path, outputFolder)
        except OSError as e:
            pass


def main():
    observer = Observer()
    event_handler = MyHandler() # create event handler
    # set observer to use created handler in directory
    observer.schedule(event_handler, path = watchFolder)
    observer.start()

    # sleep until keyboard interrupt, then stop + rejoin the observer
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
    exit(-1)

if __name__ == '__main__':
    main()
