# -*- coding: utf-8 -*-
"""lab 2_220

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1udcb-RTvMq7pQHYDV5y3SMNsYVQj_Mnt
"""

class CircularArray:
  def __init__(self, lin, st, sz):
    # Initializing Variables
    self.start = st
    self.size = sz
    self.cir = [None]*len(lin)

   
    k=self.start
    for i in range(0,self.size):
        self.cir[k]=lin[i]
        # print(self.cir[k], end=", ")
        k=(k+1)%len(self.cir)
         
  

    # if lin = [ 10,20,30,40,None]
    # then, CircularArray(lin, 2, 4) will generate
    # cir = [40, null, 10, 20, 30]
    
    # To Do. 
    # Hints: set the values for initialized variables
  
  # Print from index 0 to len(cir) - 1
  def printFullLinear(self): #Easy
    k=self.start
    for i in range(0,len(self.cir)):
      if i==len(self.cir)-1:
        print(self.cir[i])
      else:
         print(self.cir[i], end=", ")
   
    
  
  # Print from start index and total size elements
  def printForward(self):#Easy
    k=self.start
    for i in range(0,self.size):
        if i==(self.size)-1:
           print(self.cir[k])
           k=(k+1)%len(self.cir)

        else:
           print(self.cir[k], end=", ")
           k=(k+1)%len(self.cir)

  def printBackward(self): #Easy, in my dreams 
    end=(self.start+self.size-1)%len(self.cir)
    for i in range(self.size):
      if i!=self.size:
        print(self.cir[end], end=", ")
      else:
        print(self.cir[end])
      end-=1
      if end<0:
        end=len(self.cir)-1
  # With no null cells
  def linearize(self): #Medium
    k=self.start
    lin=[0]*(self.size)
    for i in range(0,self.size):
      lin[i]=self.cir[k]
      k=(k+1)%len(self.cir)
    self.cir=lin

   
  # Do not change the Start index
  def resizeStartUnchanged(self, newcapacity): #Medium
    # To Do
    self.newcuppa=newcapacity=newcapacity
    newarray=[None]*self.newcuppa
    s=self.start
    e=self.start
    for i in range(self.size):
      newarray[s]=self.cir[e]
      s=1+s
      e=(e+1)%len(self.cir)
    self.cir=newarray


  
  # This method will check whether the array is palindrome or not
  def palindromeCheck(self):#HARD
    temp = [0] * self.size
    result = True
    for x in range(self.size):
        if (self.start + x) < len(self.cir):
            temp[x] = self.cir[self.start + x]
        else:
            temp[x] = self.cir[x - (len(self.cir) - self.start)]
    for y in range(self.size // 2):
        if temp[y] != temp[-(y + 1)]:
            result = False
        else:
            pass
    if result==True:
      print("This array is a palindrome")
    else:
      print("This array is not a palindrome")


  # This method will sort the values by keeping the start unchanged
  def sort(self):
    list_x = self.cir
    for i in range(len(list_x)):
      for j in range(i + 1, len(list_x)):
        if list_x[i] != None and list_x[j] != None:
          if list_x[i] > list_x[j]:
           list_x[i], list_x[j] = list_x[j], list_x[i]
    cx = CircularArray(list_x, self.start, self.size)  
    self.cir = cx.cir
    # for i in range(self.size):
    #   for j in range(i+1, self.size):

  
  # This method will check the given array across the base array and if they are equivalent interms of values return true, or else return false
  def equivalent(self, cir_arr):
    if self.size!=cir_arr.size: 
      return False
    for elem in range(len(self.cir)):
      if self.cir[elem] not in cir_arr.cir:
        return False
    return True
  # the method take another circular array and returns a linear array containing the common elements between the two circular arrays.
  def intersection(self, c2):
        x = self.start
        y = c2.start
        list1 = []
        list2 = []
        list3 = []

        def count(list, k):
            count_r = 0
            for i in list:
                if i == k:
                    count_r += 1
            return count_r
        for i in range(len(self.cir)):
            if self.cir[x] != None:
                list1 += [self.cir[x]]
            x = (x + 1) % len(self.cir)
        for i in range(len(c2.cir)):
            if c2.cir[y] != None:
                list2 += [c2.cir[y]]
            y = (y + 1) % len(c2.cir)
        var = []
        for s in list1:
            if s not in var:
                var += [s]
        for y in var:
            max = count(list1, y)
            min = count(list2, y)
            if max > 0 and min> 0:
                if max - min == 0:
                    for i in range(min):
                        list3 += [y]

                elif max - min > 0:
                    for elem in range(max - min):
                        list3 += [y]

                elif max - min < 0:
                    for elem in range(max):
                        list3 += [y]
        return list3

# Tester class. Run this cell after completing methods in the upper cell and
# check the output

lin_arr1 = [10, 20, 30, 40, None]

print("==========Test 1==========")
c1 = CircularArray(lin_arr1, 2, 4)
c1.printFullLinear() # This should print: 40, None, 10, 20, 30
c1.printForward() # This should print: 10, 20, 30, 40
c1.printBackward() # This should print: 40, 30, 20, 10

print("==========Test 2==========")
c1.linearize()
c1.printFullLinear() # This should print: 10, 20, 30, 40

print("==========Test 3==========")
lin_arr2 = [10, 20, 30, 40, 50]
c2 = CircularArray(lin_arr2, 2, 5)
c2.printFullLinear() # This should print: 40, 50, 10, 20, 30
c2.resizeStartUnchanged(8) # parameter --> new Capacity
c2.printFullLinear() # This should print: None, None, 10, 20, 30, 40, 50, None

print("==========Test 4==========")
lin_arr3 = [10, 20, 30, 20, 10, None, None]
c3 = CircularArray(lin_arr3, 3, 5)
c3.printForward() # This should print: 10, 20, 30, 20, 10
c3.palindromeCheck() # This should print: This array is a palindrome

print("==========Test 5==========")
lin_arr4 = [10, 20, 30, 20, None, None, None]
c4 = CircularArray(lin_arr4, 3, 4)
c4.printForward() # This should print: 10, 20, 30, 20
c4.palindromeCheck() # This should print: This array is NOT a palindrome

print("==========Test 6==========")
lin_arr5 = [10, 20, -30, 20, 50, 30, None]
c5 = CircularArray(lin_arr5, 5, 6)
c5.printForward() # This should print: 10, 20, -30, 20, 50, 30
c5.sort()
c5.printForward() # This should print: -30, 10, 20, 20, 30, 50

print("==========Test 7==========")
lin_arr6 = [10, 20, -30, 20, 50, 30, None]
c6 = CircularArray(lin_arr6, 2, 6)
c7 = CircularArray(lin_arr6, 5, 6)
c6.printForward() # This should print: 10, 20, -30, 20, 50, 30
c7.printForward() # This should print: 10, 20, -30, 20, 50, 30
print(c6.equivalent(c7)) # This should print: True

print("==========Test 8==========")
lin_arr7 = [10, 20, -30, 20, 50, 30, None, None, None]
c8 = CircularArray(lin_arr7, 8, 6)
c6.printForward() # This should print: 10, 20, -30, 20, 50, 30
c8.printForward() # This should print: 10, 20, -30, 20, 50, 30
print(c6.equivalent(c8)) # This should print: True

print("==========Test 9==========")
lin_arr8 = [10, 20, 30, 40, 50, 60, None, None, None]
c9 = CircularArray(lin_arr8, 8, 6)
c6.printForward() # This should print: 10, 20, -30, 20, 50, 30
c9.printForward() # This should print: 10, 20, 30, 40, 50, 60
print(c6.equivalent(c9)) # This should print: False

print("==========Test 10==========")
lin_arr9 = [10, 20, 30, 40, 50, None, None, None]
c10 = CircularArray(lin_arr9, 5, 5)
c10.printFullLinear() # This should print: 40, 50, None, None, None, 10, 20, 30
lin_arr10 = [5, 40, 15, 25, 10, 20, 5, None, None, None, None, None]
c11 = CircularArray(lin_arr10, 8, 7)
c11.printFullLinear() # This should print: 10, 20, 5, None, None, None, None, None, 5, 40, 15, 25
output = c10.intersection(c11)
print(output) # This should print: [10, 20, 40]

string=''
k=start
for i in range(size):
  if i==size-1:
    string+=str(c[k])
    print(string)
    return
  string+=str(c[k])+'. '
  k+=1
  if k==len(c):
    k=0