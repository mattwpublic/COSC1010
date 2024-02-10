#Matthew Wideman
#COSC1010 401
#9/23/22

bobCandy = int(input("Please enter the first number:"))
aliceCandy = int(input("Please enter the second number:"))
amyCandy = int(input("Please enter the third number:"))

if bobCandy > 0 and aliceCandy > 0 and amyCandy > 0:
    
    if bobCandy > aliceCandy and bobCandy > amyCandy:
    #when bob has most candy
        
        print("The largest candy size is:", bobCandy)
        
        if bobCandy %2 == 0 and bobCandy%3 != 0:
            print("Bob is happy")
            
        elif bobCandy%2==0 and bobCandy%3==0:
            
            if bobCandy%5==0 and bobCandy%7==0:
                print("Bob is super happy")
                
            else:
                print("Bob is very happy")

        else:
            print("Bob is sad")
            
    elif aliceCandy > bobCandy and aliceCandy > amyCandy:
        #when alice has most candy
        
        print("The largest candy size is:", aliceCandy)
        
        if aliceCandy %2 == 0 and aliceCandy%3 != 0:
            print("Alice is happy")
            
        elif aliceCandy%2==0 and aliceCandy%3==0:
            
            if aliceCandy%5==0 and aliceCandy%7==0:
                print("Alice is super happy")
                
            else:
                print("Alice is very happy")
                
        else:
            print("Alice is sad")
        
    elif amyCandy > bobCandy and amyCandy > aliceCandy:
        #when amy has most candy
        
        print("The largest candy size is:", amyCandy)
        
        if amyCandy %2 == 0 and amyCandy%3 != 0:
            print("Amy is happy")

        elif amyCandy%2==0 and amyCandy%3==0:
            
            if amyCandy%5==0 and amyCandy%7==0:
                print("Amy is super happy")
                
            else:
                print("Amy is very happy")
                
        else:
            print("Alice is sad")
else:
    print("Invalid size")
    exit
