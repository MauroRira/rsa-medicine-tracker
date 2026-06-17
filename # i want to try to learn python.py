# i want to try to learn python

print("Hello, nice to meet you!")
while True:
    
    try:
        temp = int(input("What is the temperature today? "))
        
        if temp < 15:
            print("Wow, it's pretty cold today!")
        elif temp > 30:
            print("Wow, it's pretty hot today!")
        else:   
            print("The weather is pretty nice today!")
        break
    except ValueError:
            print("Please enter a valid number for the temperature.")
    

   

