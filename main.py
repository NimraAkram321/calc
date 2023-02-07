
from art import logo

def add(n1,n2):
  """this will add the numbers"""
  return n1+n2;

def subtract(n1,n2):
  """this will subtract the numbers"""
  return n1-n2;

def product(n1,n2):
  """this will multiply the numbers"""
  return n1*n2;

def divide(n1,n2):
  """this will divide the numbers"""
  return n1/n2;

operation={
  "*":product,
  "+":add,
  "-":subtract,
  "/":divide,
}
print(logo)
def calc():
  num1=float(input("enter your first number: "))
  condition =True
  for operator in operation:
      print(operator)
  while condition:
    
    operator_symbol=input("pick any operator above: ")
    num2=float(input("enter the next number: "))
    funtion=operation[operator_symbol]
    result=funtion(num1,num2);
    print(f"{num1} {operator_symbol} {num2} = {result}")    
    check=input(f"Type 'y' to continue calculation with {result}, or type 'n' for new calculation. : ").lower() 
    if check =='y':
      num1=result
    
    else:
      condition =False
      
      calc()

calc();      
    