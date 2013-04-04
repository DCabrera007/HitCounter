#! /usr/bin/python
f = open("firefox.txt", "r")
count = int(f.readline())
count+=1
f.close
f = open("firefox.txt", "w").close
f = open("firefox.txt", "w")
f.write(str(count))
f.close()

