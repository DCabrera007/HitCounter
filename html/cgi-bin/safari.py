#! /usr/bin/python
f = open("safari.txt", "r")
count = int(f.readline())
count+=1
f.close
f = open("safari.txt", "w").close
f = open("safari.txt", "w")
f.write(str(count))
f.close()

