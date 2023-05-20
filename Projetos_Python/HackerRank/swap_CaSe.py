""" 
You are given a string and your task is to swap cases. 
In other words, convert all lowercase letters to uppercase letters and vice versa.
"""

def swap_case(s):
    a =""
    for l in s:
        if l.isupper():
            a += str(l.lower())
        else:
            a += str(l.upper())
    return a

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
