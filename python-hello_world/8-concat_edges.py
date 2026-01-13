#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
# slice and rearrange
str = (str[39:67] + str[106:112] + str[:6]).strip()
print(str)
