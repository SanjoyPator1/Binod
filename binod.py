#Binod
import random
import os
import time

from colored import fg, bg, attr

#PROGRESS BAR -
print(" ")

print ('%s%s Hacking all the Binod by an another Binod :)  %s' % (fg(227),  attr('bold'),attr('reset')))

import sys

def progressbar(it, prefix="", size=60, file=sys.stdout):
    count = len(it)
    def show(j):
        x = int(size*j/count)
        file.write("%s[%s%s] %i/%i\r" % (prefix, "#"*x, "."*(size-x), j, count))
        file.flush()
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    file.write("\n")
    file.flush()
    
print(" ")
color = fg(14)

for i in progressbar(range(10), color + "  HACKING Binod : ", 40):
    time.sleep(0.2) # any calculation you need
    print(" ")

from alive_progress import alive_bar; import time

for x in 500, 400, 300, 0:
    with alive_bar(x) as bar:
        for i in range(500):
            time.sleep(0.005)
            bar()


# BINOD STRING IN WHOLE SCREEN
str = "BINOD  "

line_width = int(1000)

while True:
	for i in range(line_width):
                num = random.randint(0, 255)
                color = fg(num)
                print( color + str ,sep=' ',end=' ')
                        
                        
	print()
	time.sleep(0.5)


