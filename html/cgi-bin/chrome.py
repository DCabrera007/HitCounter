#! /usr/bin/python
f = open("chrome.txt", "r")
count = int(f.readline())
count+=1
f.close
f = open("chrome.txt", "w").close
f = open("chrome.txt", "w")
f.write(str(count))
f.close()

