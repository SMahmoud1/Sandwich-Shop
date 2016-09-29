#------------------------------------------------------------------------------
#Student Name: Salma Mahmoud/ Assignment: Project 1/ Date: 09/18/2012
#------------------------------------------------------------------------------
#Honor Code Statement: I received no assistance on this assignment that 
#violates the ethical guidelines set forth by professor and class syllabus.
#------------------------------------------------------------------------------
#References: Class Powerpoints, Textbook
#------------------------------------------------------------------------------
#Comments: Extra credit points completed
#------------------------------------------------------------------------------

print("Welcome to the Falafel Shop!")

#define name of customer, number of sandwiches, cookies, and mints ordered
name=raw_input("What is your name? ")
sandwiches=int(input("How many sandwiches would like to order today? "))
baked_goods=int(input("How many cookies would you like? "))
mints=int(input("And how many mints? "))
#define how to calculate cost of sandwiches in pennies
sandwich_cost=sandwiches*50
#define how to calculate cost of cookies
cookie_cost=baked_goods*5
#define how to calculate cost of mints
mint_cost=mints*1
#set up variables for total
hundred=0
fifty=0
twenty=0
ten=0
five=0
one=0
quarter=0
dime=0
nickel=0
penny=0
#calculate the total cost of order
total=sandwich_cost+cookie_cost+mint_cost
total1=total
if(total1>0):
#while the total is more than 10000 pennies, 1 will be added to hundred
	while(total1>=10000):
		hundred=hundred+1
#determine total once a hundred is added
		total1=total1-10000
#while the total is more than 5000 pennies, 1 will be added to fifty
	while(total1>=5000):
		fifty=fifty+1
#determine total once a fifty is added
		total1=total1-5000
#while the total is more than 2000 pennies, 1 will be added to twenty
	while(total1>=2000):
		twenty=twenty+1
#determine total once a twenty is added
		total1=total1-2000
#while the total is more than 1000 pennies, 1 will be added to ten
	while(total1>=1000):
		ten=ten+1
#determine total once a ten is added
		total1=total1-1000
#while the total is more than 500 pennies, 1 will be added to five
	while(total1>=500):
		five=five+1
#determine total once a five is added
		total1=total1-500
#while the total is more than 100 pennies, 1 will be added to one	
	while(total1>=100):
		one=one+1
#determine total once a one is added		
		total1=total1-100
#define the variable penny as the rest of the total remaining	
penny=total1
#calculate the amount due in dollars                
dollars=(hundred*100)+(50*fifty)+(20*twenty)+(10*ten)+(5*five)+one
if (penny<10):
        #print the cost due in pennies for the customer
        print("Your order will equal a total of " + str(total) + " pennies or $"+str(dollars)+".0"+str(penny))
else:
    #print the cost due in pennies for the customer
        print("Your order will equal a total of " + str(total) + " pennies or $"+str(dollars)+"."+str(penny))
#ask how they would like to pay
payment=int(input("How many pennies will you pay? "))
#define how to caluculate the change 
change=payment-total
#define how to calculate the total still needed/owe
under_pay=total-payment
#reset up variables for best change
hundred=0
fifty=0
twenty=0
ten=0
five=0
one=0
quarter=0
dime=0
nickel=0
penny=0
#determine the conditions in order to find change, amount the still owe, and if they paid the exact amount
if(change<0):
#print how much the custumer owes when payment is less than total and no service for them
	print("You still owe " + str(under_pay) + " pennies. Sorry, no food for you, " +\
	str(name) + ".")	
if(change>0):
#while the total is more than 10000 pennies, 1 will be added to hundred
	while(change>=10000):
		hundred=hundred+1
#determine total once a hundred is added
		change=change-10000
#while the total is more than 5000 pennies, 1 will be added to fifty
	while(change>=5000):
		fifty=fifty+1
#determine total once a fifty is added
		change=change-5000
#while the total is more than 2000 pennies, 1 will be added to twenty
	while(change>=2000):
		twenty=twenty+1
#determine total once a twenty is added
		change=change-2000
#while the total is more than 1000 pennies, 1 will be added to ten
	while(change>=1000):
		ten=ten+1
#determine total once a ten is added
		change=change-1000
#while the change is more than 500 pennies, 1 will be added to five
	while(change>=500):
		five=five+1
#determine change once a five is added
		change=change-500
#while the change is more than 100 pennies, 1 will be added to one	
	while(change>=100):
		one=one+1
#determine change once a one is added		
		change=change-100
#while the change is more than 25 pennies, 1 will be added to quarters		
	while(change>=25):
		quarter=quarter+1
#determine change once a quarter is added		
		change=change-25
#while the change is more than 10 pennies, 1 will be added to dimes	
	while(change>=10):
		dime=dime+1
#determine change once a dime is added		
		change=change-10
#while the change is more than 5 pennies, 1 will be added to nickels		
	while(change>=5):
		nickel=nickel+1
#determine change once a nickel is added		
		change=change-5
#define the variable penny as the rest of the change remaining		
	penny=change
#calculate the change in dollars   
dollars_change=(hundred*100)+(50*fifty)+(20*twenty)+(10*ten)+(5*five)+one
#calculate the cents change   
cents=penny+(dime*10)+(nickel*5)+(quarter*25)
if (cents<10):
#print the customer's change and greet them out	while thanking them
        print("Your change will be $"+str(dollars_change)+".0"+str(cents)+" which would be "+ str(hundred) +" hundreds, "\
              + str(fifty) +" fifties, "+ str(twenty) +" twenties, "+ str(ten) +" tens, "+ str(five) +" fives, "\
              +str(one)+" ones, " + str(quarter) + " quarters, " + str(dime) + " dimes, " \
              + str(nickel) + " nickles, and " + str(penny) + " pennies. "\
                "Thank you for visiting the Falafel Shop. Hope to see you "\
                + "again soon, " + str(name) + "!")
else:
#print the customer's change and greet them out	while thanking them
        print("Your change will be $"+str(dollars_change)+"."+str(cents)+" which would be "+ str(hundred) +" hundreds, "\
              + str(fifty) +" fifties, "+ str(twenty) +" twenties, "+ str(ten) +" tens, "+ str(five) +" fives, "\
              +str(one)+" ones, " + str(quarter) + " quarters, " + str(dime) + " dimes, " \
              + str(nickel) + " nickles, and " + str(penny) + " pennies. "\
                "Thank you for visiting the Falafel Shop. Hope to see you "\
                + "again soon, " + str(name) + "!")
#define condition when customer pays the exact amount	
if(change==0):
#print a greeting out for the customer and thanking them
	print("You paid with exact change with a total of " + str(total) + \
	" pennies. Thank you for visiting the Falafel Shop. Hope to see you " + \
	"again soon, " +str(name) + "!")
