emptylist = []
markslist = [80,90,100,100,90,80]
print(markslist)

Samplelist = [1, 2, 3, 5, 9]
reapetedlist = Samplelist*3
print(reapetedlist)

print(len(markslist))
print(markslist[0])
print(markslist[-1])
print(markslist[0:2])

def palindrone(markslist):
    e = len(markslist) -1
    s = 0

    while(s<e):
        if(markslist[s]!=markslist[e]):
            return False
        s+=1
        e-=1
        return True
    
    
if(palindrone(markslist)):
        print("Its a palindrone")
else:
        print("its not a palindrone")

total_marks = 0

for mark in markslist:
      total_marks += mark
print("Total Marks",total_marks)

lenth = len(markslist)
total_marks
total_marks = total_marks/lenth
print("Average",total_marks)

print("Smallest value in the list ",markslist[0])
print("The largest value in the list",markslist[3])

