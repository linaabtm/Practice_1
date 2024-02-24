letter,number=map(input().split(''))
countl=0
countn=0
if letter==['a','c','e','g']:
    countl+=1
if number%2==0:
    countn+=1
if countl==0 and countn==0:
    print('black')
if countl==1 and countn==0:
    print('white')
if countl == 0 and countn == 1:
    print('white')
if countl == 1 and countn == 1:
    print('black')