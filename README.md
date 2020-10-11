1.Largest number:

list= [12,24,5,48,99]
Print("largest element is :", max(list))


2. Second largest number:

list= [12,24,5,48,99]
max= max(list[0], list[1])
secondmax= min(list[0], list[1])
  For i in range (2, len(list)):
     if list[i]> max:
        Secondmax= max
         max= list[i]
     elif list[i] > second max:
        secondmax= last[i]
Print("second highest number is:", str(secondmax))


3. Merge two lists and sort:

list=[12,24,5,48,99]
list1=[20,10,5]
list.extend(list1)
Print(list)
list.sort()
print("sorted list is :", list)

4. Swap first and last digit in list:

list1= [12, 24, 5,48,99]
def swaplist(list1):
    first = list1.pop(0)
    Last= list1.pop(-1)
    list.insert(0,Last)
     list.append(first)
 return list1
