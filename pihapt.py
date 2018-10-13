#!/usr/bin/python3

import subprocess
import tkinter as tk

from drv2667 import drv2667

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.start = tk.Button(self, text="      start      ",
                                command=self._start_video)
        self.start.pack(side=tk.LEFT, fill=tk.X)

        self.quit = tk.Button(self, text="      stop       ",
                              command=self._stop_video)
        self.quit.pack(side=tk.LEFT, fill=tk.X)

        self.up = tk.Button(self, text="      up       ",
                              command=self._volume_up)
        self.up.pack(side=tk.LEFT, fill=tk.X)

        self.down = tk.Button(self, text="     down     ",
                              command=self._volume_down)
        self.down.pack(side=tk.LEFT, fill=tk.X)

    def _start_video(self):
        print("Start video")
        command = 'omxplayer /home/pi/piHapt/asset/sl.mov --loop'
        self.proc = subprocess.Popen(command,shell=True,stdin=subprocess.PIPE, universal_newlines=True)

    def _stop_video(self):
        self.proc.communicate(input='q')

    def _volume_up(self):
        self.proc.communicate(input='+')

    def _volume_down(self):
        self.proc.communicate(input='-')

root = tk.Tk()
app = Application(master=root)
app.mainloop()
