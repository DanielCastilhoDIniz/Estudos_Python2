""" 
Given the participants' score sheet for your University Sports Day, you are required 
to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

Input Format

The first line contains . The second line contains an array   of  integers each separated by a space.

Output Format

Print the runner-up score.
"""

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    lista = (list(arr))
    a = max(lista)
    b = sorted(lista)
    m = n-1
    while True:
        if b[m] < a:
            print(b[m])
            break
        else:
            m -= 1
