#ITEM DISCOUNT CALC

#while True:
 #   itemPrice = input("Please enter an item price: ")
  #  if itemPrice == 'DONE':
   #     break
    #discountPrice = float(itemPrice) - (float(itemPrice)/5)
    #print(discountPrice)

####################################################################

#TEST SCORE AVG CALC
   
while True:
    testScore1 = input("Please enter a test score: ")
    testScore2 = input("Please enter a test score: ")
    testScore3 = input("Please enter a test score: ")
    if testScore1 == 'DONE' or testScore2 == 'DONE' or testScore3 == 'DONE':
        break
    scoreAverage = (float(testScore1) + float(testScore2) + float(testScore3))/3
    print(scoreAverage)
