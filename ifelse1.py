
import math
import os
import random
import re
import sys

'''if __name__ == '__main__':
    n = int(input().strip())
    
    if n % 2 == 1:
        print('Weird')
    elif n % 2 == 0 and 2 <= n <= 5:
        print("Not Weird")
    elif n % 2 == 0 and 6 <= n <= 10:
        print('Weird')
    elif n % 2 == 0 and n > 20:
        print("Not Weird")
    else:
        print("Not Weird")'''
if __name__ == '__main__':
    n = int(input().strip())
    
    if n%2 ==0:
        if n>=2 and n<=5:
            print("Not Weird")

        elif n>=6 and n<=20:
            print("Weird")

        elif n>20:
            print("Not Weird")

    else:
        print("Weird")
