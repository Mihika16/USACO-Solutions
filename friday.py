"""
ID: mihika.1
LANG: PYTHON3
PROB: friday

"""

fin = open("friday.in", "r")
ans = open("friday.out", "w")

counterarr = [0, 0, 0, 0, 0, 0, 0]
data = (fin.read()).split(' ')
N = data[0]
N = int(N)

enddate = 1900+N-1
dayIndex = 1;


for y in range(1900, enddate+1):
    for m in range(1,13):
        if m == 9 or m == 4 or m == 6 or m == 11:
            endD = 30

        elif m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
            endD = 31

        elif m == 2:
           endD = 28
           if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
               endD = 29
             

        for d in range(1,endD+1):
            #control dayIndex
            dayIndex = (dayIndex + 1) % 7
            
            #increase counter[dayIndex] ++ if d is 13
            if d == 13:
                counterarr[dayIndex] += 1

answer = ' '.join([str(elem) for elem in counterarr]) 

ans.write(''.join(answer)+'\n')

fin.close()
ans.close()
