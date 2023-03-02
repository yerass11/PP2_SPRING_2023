import re   
  
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
  
def check(email):   
  
    if(re.search(regex,email)):   
        print("Valid Email")   
    else:   
        print("Invalid Email")   
      
if __name__ == '__main__' :   
      
    email = "rohit.gupta@mcnsolutions.net"  
    print("1.")
    check(email)   
  
    email = "praveen@c-sharpcorner.com"  
    print("2.")
    check(email)   
  
    email = "inform2atul@gmail.net"  
    print("3.")
    check(email)  
    
    email = "y_saiman@kbtu.kz"  
    print("4.")
    check(email)  