#! /usr/bin/python
f = open("ie.txt", "r")
count = int(f.readline())
count+=1
f.close
f = open("ie.txt", "w").close
f = open("ie.txt", "w")
f.write(str(count))
f.close()

