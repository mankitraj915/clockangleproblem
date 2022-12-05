d=("<<<========Clock Angle Problem Python Mini Project========>>>")
print(d)
print("Enter 1 for Know time")
print("Enter 2 for Angle between  hour and minute hand")
print("Enter 3 for Find another problem")
choice=int(input("Enter the choice: "))
def calcAngle(h,m):
    if (h<0 or m<0 or h>12 or m>60):
        print("Wrong input")
    if (h==12):
        h=0
    if (m==60):
        m=0
    hours_angle=0.5*(h*60+m)
    minute_angle=6*m
    angle=abs(hours_angle - minute_angle)
    angle=min(360-angle,angle)
    return angle
if choice ==1:
    h=int(input("Enter hours: "))
    m=int(input("Enter minutes: "))
    print("TIME IS",h,':',m)
    choice=int(input("Enter the choice: "))
    print('Angle: ',calcAngle(h,m),'°')
    
elif choice==2:
    h=int(input("Enter hours: "))
    m=int(input("Enter minutes: "))
    print('Angle: ',calcAngle(h,m),'°')
elif choice==3:
    h=int(input("Enter hours: "))
    m=int(input("Enter minutes: "))
    print('Angle: ',calcAngle(h,m),'°')
    choice=int(input("Enter the choice: "))
    h=int(input("Enter hours: "))
    m=int(input("Enter minutes: "))
    print("TIME IS",h,':',m)
    print('Angle: ',calcAngle(h,m),'°')
elif choice>3:
    print("TRY AGAIN")
    choice=int(input("Enter the choice: "))
    h=int(input("Enter hours: "))
    m=int(input("Enter minutes: "))
    print("TIME IS",h,':',m)
    choice=int(input("Enter the choice: "))
    print('Angle: ',calcAngle(h,m),'°')
else:
    print("THANK YOU")
    
    
