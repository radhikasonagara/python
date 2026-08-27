x = 10 # Global variable
def show():
 x = 5 # Local variable
 print("Local x:", x)
def display():
 global x
 x = x + 5
 print("Modified Global x:", x)
show()
display()
print("Global x after function call:", x)