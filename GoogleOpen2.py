import webbrowser

count = 0

import os
dir = os.path.expanduser('C://Users//kpete//Documents//Python codes//dist//GoogleOpen1')
os.chdir(dir)

# Python program to count the  
# number of lines in a text file 
  
  
# Opening a file 
file = open("GoogleOpenSites.txt","r") 
Counter = 0
  
# Reading from file 
Content = file.read() 
CoList = Content.split("\n") 
  
for i in CoList: 
    if i: 
        Counter += 1




#search 1
with open("GoogleOpenSites.txt") as fp:  
    for i in range (Counter):
        count += 1
        line = fp.readline()

        url =line.replace(" ","+")

        webbrowser.register('chrome',
            None,
            webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
        webbrowser.get('chrome').open(url)

