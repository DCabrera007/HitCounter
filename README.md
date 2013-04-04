HitCounter
==========

This is a simple php script that calls multiple python scripts in order to keep track of the number of visitors on a page and how many of those visitors are using which browser. The data is stored in separate text files and there is a python script used to modify each file. Specifically chrom.py adds 1 to chrome.txt if the user is using chrome, firefox.py adds 1 to firefox.txt if the user is using firefox, ie.py adds 1 to ie.txt if the user is using internet explorer, and safari.py adds 1 to safari.txt if the user is using safari. The script incr.py adds 1 to text.txt whenever a user visits the page. Finally, getr.py prints the contents of tex.txt. The php page just calls these various scripts in order to display the information to the user.
