import random
import sys
import datetime
from time import sleep

# get results and statistics
def status(records):
    bestTime = 100
    worstTime = 0
    wins = 0
    correct = 0
    for rec in records:
        print(rec)
        if rec[4] == True:
            wins += 1
        if rec[1] < bestTime:
            bestTime = rec[1]
        if rec[1] > worstTime:
            worstTime  = rec[1]
        if rec[2] == rec[3]:
            correct += 1
    pct = ((wins/20)*100)
    print("Best time:",bestTime)
    print("Worst time:",worstTime)
    print("Correct:",correct)
    print("Wins: " + str(wins)+ "("+str(pct)+"%)")

# get an array of 3 unique random numbers
# techically this could still return an array with
# two equal distances
def getSet():
    arr = [0,0,0]
    for y in range(3):
        test_set = set(arr)
        while arr[y] == 0:
            a = random.randrange(1,16)
            if a in test_set:
                continue
            else:
                arr[y] = a
                a = 0
    return arr

# calculate the winning number
def getVals(arr):
    win = 0
    arrSort = sorted(arr)
    #print(arrSort, end=' ')
    if (arrSort[1] - arrSort[0]) > (arrSort[2] - arrSort[1]):
        win = arrSort[0]
    else:
        win  = arrSort[2]
    return win
    
    

def main():
    print("\nGIA numeracy practice test\n")
    print("You will be presented with 20 sets of three numbers. \nFor each set of numbers, find the middle number.")
    print("Then select the number furthest away from that number.\n")
    print("For example, in the set [4,2,8] the middle number is 4.")
    print("the difference between 2 and 4 is 2, and the difference between 4 and 8 is 4.")
    print("In this instance, the winning number is 8.")
    print("In the instance that two numbers have an equal value, choose the highest.\n")
    print("You will be tested for speed as well as accuracy. \nPlease complete each set in under 5 seconds.\n")
    start = input("Start test? y/n\n")
    if start.lower() == 'y':
        print("Starting in ", end='')
        for x in range(3,0,-1):
            print(str(x)+"...",end='')
            sleep(1)
    else:
        sys.exit("exiting...")
    print("\n")
    rec = []
    for x in range(20):
        win = False
        numset = getSet()
        print(numset)
        start = datetime.datetime.now()
        choice = input("Your choice: ")
        hi = getVals(numset)
        end = datetime.datetime.now()
        diff = end - start
        secs = round(diff.total_seconds(),2)
        if (int(choice) == hi) and (secs < 5):
            win = True
        rec.append([numset, secs, int(choice), hi, win])

    status(rec)

main()
