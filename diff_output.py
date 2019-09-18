#!/usr/bin/env python

import difflib
text1 = open("pre_test.txt").readlines()
text2 = open("post_test.txt").readlines()

#for line in difflib.unified_diff(text1, text2):
#    print(line)


diff = difflib.ndiff(text1,text2)
print("".join(diff),)