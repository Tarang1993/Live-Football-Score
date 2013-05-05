import urllib
import urllib2
import StringIO
import xml.dom.minidom
from Tkinter import *
import tkMessageBox
from xml.dom import minidom
url = "http://www.scorespro.com/rss/live-soccer.xml"
u = urllib2.urlopen(url)
xml = minidom.parse(u)
s=''
def showScore():
    s=''
    for element in xml.getElementsByTagName('title'):
        s=s+element.firstChild.nodeValue
        s=s+'\n'
    return s
root = Tk()
root.title("Live Soccer Score!")
score = showScore()
var = StringVar()
soccer_score = Message(root , textvariable = var , relief = RAISED)
var.set(score)
soccer_score.pack()
root.mainloop()
