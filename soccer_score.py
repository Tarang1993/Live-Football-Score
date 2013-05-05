# Author : Tarang Patel
# Email  : tarangrockr@gmail.com

#!/usr/bin/python


import urllib
import urllib2
import StringIO
import xml.dom.minidom
from Tkinter import *
import commands
import sys
from subprocess import call
import tkMessageBox
from xml.dom import minidom
from time import sleep
import threading

time = 300

def showScore():
    url = "http://www.scorespro.com/rss/live-soccer.xml"
    u = urllib2.urlopen(url)
    xml = minidom.parse(u)
    s=''
    for element in xml.getElementsByTagName('title'):
        s=s+element.firstChild.nodeValue
        s=s+'\n'
    return s


def main():
    str="notify-send \"" + showScore() + "\""
    commands.getstatusoutput(str)

class Window(threading.Thread):
	def __init__(self):
         
                threading.Thread.__init__(self)
                self.start()
        def callback(self):
                self.root.quit()

        def run(self):
                self.root = Tk()
                self.root.title("Live Soccer Score!")
                score = showScore()
                self.var = StringVar()
                soccer_score = Message(self.root , textvariable = self.var , relief = RAISED)
                self.var.set(score)
                soccer_score.pack()

		self.root.mainloop()

window = Window()
	
while True:
    if __name__ == "__main__":
        main()
        sleep(time)
    
