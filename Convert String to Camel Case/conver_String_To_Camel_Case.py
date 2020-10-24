# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 23:45:25 2020

@author: HP

Solution of: https://www.codewars.com/kata/517abf86da9663f1d2000003/train/python
"""

def to_camel_case(text):
    text = list(text)
    ans = []
    emp = ''
    for i in range(len(text)):
        if text[i] == '-' or text[i] == '_':
            i += 1
            text[i] = text[i].upper()
            continue
        ans.append(text[i])
    text = emp.join(ans)
    return text
    
    


text = input()
print("The answer is: " + to_camel_case(text))