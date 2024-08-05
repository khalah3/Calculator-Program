
#calculator

def add(n1,n2):
  return n1+n2

def subtract(n1,n2):
  return n1-n2

def multiply(n1,n2):
  return n1*n2

def divide(n1,n2):
  return n1/n2

dictionary={'+':add,'-':subtract,'*':multiply,'/':divide}

from replit import clear

for key in dictionary:
  print(key)


Program_run=True
  
while Program_run==True:

    num1=float(input('enter the first number:  '))
    num2=float(input('enter the second number:  '))
    
    def Calculation(num1,num2):
      
      operation=input('Please enter the operation you want to perform\n')
      calculator=dictionary[operation]
      result=calculator(num1,num2)
      return result
      print(result)
    
    
    More_calculation=True
    
    result=Calculation(num1,num2)
    print(result)
    
    
    while More_calculation==True:
      continue_operations = input('Do you want to perform another operation on the results\n')
      if continue_operations == 'yes':
        new_number=float(input('enter the new number:\n '))
        new_result=Calculation(result,new_number)
        result=new_result
        print(result)
      elif continue_operations == 'no':
        clear()
        More_calculation=False
        Program_run=True
    
    
    
    
    
    
    
    
    
  
  






