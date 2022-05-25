import random 
def process():
  print("election by bully")

  ch = [1,0]
  p = [(1,6,0),(2,3,0),(3,6,0),(4,4,0)]
  #id,priority,status(leader or not)
  print("Processes in the system are :-")
  print("id\tPriority")
  for i in p:
    print(i[0],'\t',i[1])
  print()
  p_copy = list()
  for i in p:
    p_copy.append(i)
  # n = 4
  
  c =0
  while c!=1 or len(p) == 0:
    print("\n\n\nInitiated Election")
    mpri = 0
    mprili = list()
    for i in range(len(p)):
      if p[i][1] > mpri:
        mprili.clear()
        mprili.append(p[i])
        mpri = p[i][1]
      elif p[i][1] == mpri:
        mprili.append(p[i])
    #selecting the process with highest priorities
    winner = random.choice(mprili)
    print("Winner selected has priority =",winner[1])
    print("Winner id = ",winner[0])
    c= random.choice(ch)
    if c==1:
      for i in range(len(p)):
        if p[i][0] != winner[0]:
          print("Victoy message sent to process id ",p[i][0])
      print("Victory Messages sent successfully")
    elif c==0:
      print("Failed to send victory messages, starting re- election")
      p.remove(winner)
  
  if len(p) == 0:
    print("All processes failed to be coordinator ")
  else:
    print("Hence the new coordinator is process number :",winner[0])

def memory():
  print("Central Server Algorithm ")
  mem={ 'name':'abcd' , 'file_size': 10 , 'text': 'hello world'}
  
  req = [(1,'r','name'),(3,'w','file_size'),(8,'w','text'),(9,'r','name'),(2,'r','file_size'),(5,'r','text')]
  #client no, read or write, memory AttributeError
  entity = {"r":"read","w":"write"}
  print("Requests are as follows")
  print("id\tRequest\tEntity")
  for i in req:
    print(i[0],'\t',entity[i[1]],'\t',i[2],'\n')
  for i in req:
    if i[1] == 'r':
      print('Client ',i[0],' wants to read ',i[2])
      print(i[2],' = ',mem[i[2]])
      
    elif i[1] == 'w':
      print('Client ',i[0],'wants to write data in ',i[2])
      print('Write data for ',i[2],':')
      s =input()
      mem[i[2]] = s
    
  print()

def io_manage():
  print("N Step Algorithm") 
  cuu = 54
  requests = [10,98, 137, 122, 183, 14, 133, 65, 78,8,44] #all requests
  
  n = 3
  print("Requests are:- ")
  for i in requests:
    print(i,end = '\t')
  print()
  def scan(req,cuu):
      cu = cuu
      s =0
      print("Current head position = ",cu)
      print("Requests = ",end=' ')
      for i in req: print(i,end=' ')
      print()
  
      ll=0 #lower_limit 
      hl = 200 #higher_limit
      if cuu == ll:
        req.append(hl)
      elif cuu == hl:
        req.append(ll)
      else:
        req.append(ll)
        req.append(hl)
      
      req.sort()
      #print(reqs)
      print("From\t->\tTo")
    
      for i in range(len(req)-1,-1,-1):
          if(req[i]<cuu):
              s = s+ abs(cu-req[i])
              
              print( cu,'\t->\t',req[i])
              cu = req[i]
              
            
      for i in range(len(req)):
          if(req[i]>=cuu):
              
              s = s+ abs(cu-req[i])
              
              print( cu,'\t->\t',req[i])
              cu = req[i]
              
      
  
      print("Distance traversed= ", s)
      return cu,s
  reqs = list()
  x=1
  total_dist = 0
  reqs.append(requests[0])
  for i in range(1,len(requests)):
      reqs.append(requests[i])
      if i%n==n-1 or i == len(requests)-1:
          print("\n\n")
          print("servicing batch number: ",x)
          x=x+1
          cuu,a = scan(reqs,cuu)
          total_dist = total_dist+a
          reqs.clear()
  print("Final Total distance = ", total_dist)


def file():
  print("Sequential Update Algorithm") 
  #import random
  # id, key
  #delete 0 ,revise 1 , add2
  old = [[1,10,0],[2,13,0],[3,14,0],[4,16,0],[5,20,0],[6,21,0],[7,22,0],[8,25,0],[9,35,0]]
  trans = [[1,14,1],[2,17,2],[3,18,2],[4,21,0],[5,23,2],[6,25,1],[7,31,2]] #id,key, type 
  new = list()
  
  name = {0:'D',1:"R",2:"A"}
  print("Keys of transaction are :")
  print("id\tkey\ttype")
  for i in trans:
    print(i[0],'\t',i[1],'\t',name[i[2]])
  
  print("Keys of Old Master file are :")
  print("id\tkey")
  for i in old:
    print(i[0],'\t',i[1],'\t')
  
  i = 0 #old
  j = 0 #trans
  while i != len(old)-1 or j!= len(trans)-1:
    # print(" trans = ", trans[j][1], '\t old', old[i][1])
    # print('i = ',i,' \t j = ',j)
    if trans[j][1] > old[i][1]:
      new.append(old[i])
      i = i+1
    elif trans[j][1] < old[i][1]:
      new.append(trans[j])
      j= j+1
    elif trans[j][2] == 0:
      print("Transaction ",trans[j][0]," deletes file ",old[i][0])
      j = j+1
      i = i+1
    elif trans[j][2] == 1:
      print("Content of Master file changed according to transaction ",trans[j][0])
      j = j+1
      i = i+1
      new.append(trans[j])
      
    elif trans[j][2] == 2:
      print("Transaction ",trans[j][0]," causes an adding error, contents could not be updated")
      i = i+1
      j = j+1
  
  print("Keys of New Master file are :")
  print("id\tkey")
  for i in range(len(new)):
    new[i][0] = i+1
    print(new[i][0],'\t',new[i][1],'\t')
    
def menu():
  print("\n\n\n")
  print("Enter 0 to end")
  print('Enter 1 for File Management')
  print("Enter 2 for Memory Management")
  print('Enter 3 for I/o Management')
  print('Enter 4 for Process Management')
n = 1
while n!=0:
  menu()
  n = int(input())
  print("--------------------------------------")
  if n ==1: 
    # call file
    print('file')
    file()
  elif n == 2:
    #call memory
    print('Memory')
    memory()
  elif n==3:
    print('I/o')
    io_manage()
  elif n ==4:
    print('Process')
    process()
  elif n ==0:
    print("Thank you for using our OS")
  else:
    print('Wrong Input')
