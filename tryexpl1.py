#!/usr/bin/python
# -*- coding: utf-8 -*-
#filename:

#try...except

'''import sys
try:
    s = raw_input("enter something:")
except EOFError:
    print 'Error input'
    sys.exit()
print s '''

#try...finally

'''import time
try:
    f = file('poem.txt')
    while True:
        line = f.read_lines()
        if len(line) == 0:
            break
        time.sleep(2)
        print line 
finally:
    f.close()
    print "Cleaning up"'''
    
#多层测试
'''
l = [1,2,3,4]

try:
    print [6]
except:
    print "Error"
else:
    print "No error"
     '''
    
def safe_float(obj):
    try:
        retval = float(obj)
    except(ValueError, TypeError), diag:
        retval = str(diag)
    return retval

print safe_float("11.4")
print safe_float("yes")
        
        
        
        
    









    