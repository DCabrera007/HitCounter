#! /usr/bin/python
f = open("text.txt", "r")
count = int(f.readline())
count+=1
f.close
f = open("text.txt", "w").close
f = open("text.txt", "w")
f.write(str(count))
f.close()

