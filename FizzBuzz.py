#gitItPretty branch. In this branch I'll be adding some comments as well as putting 
#the code in a method inside a class. 


#Create the class
class fizzBuzz:
    #Start of fizzBuzz method.
    def fizzBuzz():
        #for loop to count from 1 to 100
        for x in range(1, 101):
            #takes the current number in the for loop and divides it by three. Then checks to see if the remainder is 0.
            if x%3 == 0:
                #if the number is divisible by 3 it will check to see if it's also divisible by 5
                if x%5 == 0:
                    print("FizzBuzz")
                else:
                    print("Fizz")
            #this line checks to see if the line is divisible by 5
            elif x%5 == 0:
                print("Buzz") 
            #finally if it's not divisible by 3 or 5 it just prints the number
            else:
                print(x)
#calls the method
fizzBuzz.fizzBuzz()


