
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

num1=int(input("enter your first number: "))


for operator in operation:
  print(operator)
operator_symbol=input("pick any operator above: ")
num2=int(input("enter your second number: "))
funtion=operation[operator_symbol]
result=funtion(num1,num2);
    
print(f"{num1} {operator_symbol} {num2} = {result}")    

operator_symbol=input("pick an other operator: ")
num3=int(input("enter the next number: "))
funtion=operation[operator_symbol]
num4=result
result=funtion(num4,num3)

print(f"{num4} {operator_symbol} {num3} = {result}")
