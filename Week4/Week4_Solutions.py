## ============== NOTE - START ============== ##
## I have added code solutions to week 4 here
## because the project descriptions are attrocious
## and any newbie to py will find this must unpleasant
## thus, the solutions.
## ============== NOTE - END ============== ##

## ============== 4.1 ============== ##
# N/A

## ============== 4.2 ============== ##
# N/A

## ============== 4.3 ============== ##
# N/A

## ============== 4.4 ============== ##
def test() : # do not change this line!
  values = [4, 7, 8, 9, -5] # do not change this line!
  
  # write your code here so that it modifies values
  if values[-1] < 0:
    values.pop(-1)
  # be sure to indent your code!
  values.insert(1,(values[0]+values[1])/2)
  e = values.pop()
  s = values.pop(0)
  values.insert(0,e)
  values.insert(len(values),s)
  
  print(values)
  return values # do not change this line!
# do not write any code below here  

test()  # do not change this line!
# do not remove this line!

## ============== 4.5 ============== ##
## Part 1
def test() : # do not change this line!
  list = [4, 5, 1, 9, -2, 0, 3, -5] # do not change this line!
  min1 = list[0]
  min2 = list[1]

  # write your code here so that it sets
  # min1 and min2 to the two smallest numbers
  # be sure to indent your code!
  
  ## Approach 1:
  #list.sort()
  #min1,min2 = list[:2]
  ## Approach 2:
  min1=min(list)
  list.remove(min1)
  min2=min(list)

  print(min1, min2)
  return (min1, min2) # do not change this line!
# do not write any code below here  

test() # do not change this line!
# do not remove this line!

## Part 2
def test() : # do not change this or the next line!
  numbers = [11.5, 28.3, 23.5, -4.8, 15.9, -63.1, 79.4, 80.0, 0, 67.4, -11.9, 32.6]
  average = 0

  # write your code here so that it sets average
  # to the average of the non-negative numbers
  # be sure to indent your code!
  ## note: nice trick on teh bullshit about zero, folks.
  posl = [x for x in numbers if x >= 0]
  average = sum(posl) / len(posl)

  print(average)
  return average # do not change this line!
  # do not write any code below here  

test()  # do not change this line!
# do not remove this line!

## ============== 4.6 ============== ##
def verify(number) : # do not change this line!
  status = False
  nx = [int(x) for x in number if x.isdigit()]
  # write your code here so that it verifies the card number
  if (nx[0] != 4):
    status = 1
  else:
    if ((nx[3]-nx[4]) != 1):
      status = 2
    else:
      if (sum(nx) % 4):
        status = 3
      else:
        if ((10*(nx[0]+nx[6])+nx[1]+nx[7]) != 100):
          status = 4
        else:
          status = True
  # be sure to indent your code!
  
  return status # modify this line as needed

input = "4503-2055-0000" # change this as you test your function
output = verify(input) # invoke the method using a test input
print(output) # prints the output of the function
# do not remove this line!

## ============== 4.6 - challenge ============== ##
def check_format(number) : # do not change this line!

  # write your code here so that it verifies the number format
  if (number[:4].isdigit()) \
    and (number[5:9].isdigit()) \
      and (number[-4:].isdigit()) \
        and (len(number) == 14) \
          and (number[4] == '-') \
            and (number[9] == '-'):
              return True
  # be sure to indent your code!
  
  return False # modify this line as needed

input = "1345-9840-6480"
output = check_format(input) # invoke the method using a test input
print(output) # prints the output of the function
# do not remove this line!

## ============== 4.7 ============== ##

# implement County class here
class County:
    def __init__(self,name,population,voters):
      self.name=name
      self.population=population
      self.voters=voters

def highest_turnout(data) :

  # implement the function here
  high_pct = 0
  high_county = ''
  for obj in data:
      pct_vote = float(obj.voters)/float(obj.population)
      if pct_vote > high_pct:
        high_pct = pct_vote
        high_county = obj.name

  return (high_county,high_pct)# modify this as needed

# your program will be evaluated using these objects 
# it is okay to change/remove these lines but your program
# will be evaluated using these as inputs
allegheny = County("allegheny", 1000490, 645469)
philadelphia = County("philadelphia", 1134081, 539069)
montgomery = County("montgomery", 568952, 399591)
lancaster = County("lancaster", 345367, 230278)
delaware = County("delaware", 414031, 284538)
chester = County("chester", 319919, 230823)
bucks = County("bucks", 444149, 319816)
data = [allegheny, philadelphia, montgomery, lancaster, delaware, chester, bucks]  

result = highest_turnout(data) # do not change this line!
print(result) # prints the output of the function
# do not remove this line!

## ============== 4.8 ============== ##
def search(keyword) :

   # implement the function here
  kwl = []
  kwl.append(keyword)
  for t_itm in Thesaurus:
    if t_itm.word == keyword:
      for syn in t_itm.synonyms:
        kwl.append(syn)
  tpl = []
  for word in kwl:
    word_cnt = 0
    for doc in Corpus:
      word_cnt+=doc.count(word)
    tpl.append((word,word_cnt))

  return tpl # modify to return a list of tuples

input = "happy"
output = search(input) # invoke the method using a test input
print(output) # prints the output of the function
# do not remove this line!
