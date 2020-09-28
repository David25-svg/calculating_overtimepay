"""this project is calculating the gross pay of an employee.
it Starts with the base hours to work for the week as being 40hrs and the overtime rate as double (2).
the program Request the employee id, the number of hours worked for the week, and also the amount of money paid per hour (hourly pay rate).
With this information, if the employee works more than 40 hrs that week,
the program prints using a sentence with the name and id of the employee, the gross pay including the overtime.
If there is no overtime, then the program just displays the employee's name, id and gross pay.
"""

Fullname= input('Enter Full Name: ')#asking the user to input Full Name 
Id= int(input('Enter ID number: ')) #asking the user to input Work ID
h= int(input('enter number of hours worked: '))#asking the user to input the number of hours worked
if h>=40:#if the hours worked grater than base hour calculate pay
    hourly=18#hourly rate
    pay=(h*hourly)#formula to calculate income
    print (Fullname,'your pay amonunt is:',pay,)#prints out full name and calculated pay amonunt
    o=int(input('enter number of hours worked overtime if any if not enter 0:'))#asking the user to input overtime hours worked if any
    if o!=0:#if the over time hours does not equal zero calculate overtime pay
        newa=(o*hourly+pay)#formula to calculate ovetime income
        print (Fullname,'your amout plus overtime is:',newa,)#prints out fulll name and calculated overtime amout
        
else:#this else function is theres no overtime to clculate
    h
    hourly=18
    m=(h*hourly)
    print (Fullname,'Your pay amount is:',m,)
#this is allwong the program to run twice, calculating a second income   
on= input('Do You want To Calculate another gross pay,y for yes,n for no:')
if on=='y':
    Fullname= input('Enter Full Name:')#asking the user to input Full Name 
    Id= int(input('Enter ID number:'))#asking the user to input Work ID 
    h= int(input('enter number of hours worked:'))#asking the user to input the number of hours worked

    if h>=40:#if the hours worked grater than base hour calculate pay
        hourly=18#hourly rate
        pay=(h*hourly)#formula to calculate income
        print (Fullname,'your pay amonunt is:',pay,)#prints out full name and calculated pay amonunt
        o=int(input('enter number of hours worked overtime if any if not enter 0:'))#asking the user to input overtime hours worked if any
        if o!=0:#if the over time hours does not equal zero calculate overtime pay
            newa=(o*hourly+pay)#formula to calculate ovetime income
            print (Fullname,'your amout plus overtime is:',newa,)#prints out fulll name and calculated overtime amout 
    else:#this else function is theres no overtime to clculate
        h
        hourly=18
        m=(h*hourly)
        print (Fullname,'Your pay amount is',m,)
    
