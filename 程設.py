 #display two messager
print('learning python now')
print('python is fun')
#convert Fahrenheit to Celsius
print('Fahrenheit 80 is Celsius degree')
print(5/9*(80-32))
#試題
print('Fahrenheit 100 is Celsius degree')
print(5/9*(100-32))
#試題1
print('feet 90 is meter')
print(90*305/10000)
#2-1
print(12345)
print(123.456)
print('learning python now!')
print('python is fun')
print('let\'s go')
print('\\n is skip a lie')
print('radius=',12)
print('hello,',end='')
print('world')
print('hello,','world')
print('hello,',end='***')
print('world')
print('***hello,world',end='***')
print('')
print('helll,python')
print('excellenyt')
#2-2
print(format(1.23456,'10.2%'))
print(format(12.3456,'8.3f'))
print(format('python is fun','15s'))
print(format('python is fun','>15s'))
print(12345,12,1234567)
print('|%8.2f|'%(123.456))
print('|%.2f|'%(123.456))
print('|%30s|'%('learning python now'))
print('|%-30s|'%('learning python now'))
print('|%15s|'%('learning python now'))
#3-2-1
a=7+8*2-6+8/2
print(a)
b=(7+8)*2-(6+8)/2
print(b)
st1='learning python'+'is fun'
print(st1)
st2='learning python'\
     'is fun'
print(st2)
question1='is your birthday?\n'+\
           '1 3 5 7\n'+\
           '9 11 13 15\n'+\
           '17 19 21 23\n'+\
           '25 27 29 31\n'+\
           'enter 1 for yes and 0 for no'
print(question1)
print(8/3)
print(8//3)
print(8**2)
print(100**0.5)
print(8%2)
i=100
j=100
k=100
print(i,j,k)
i=j=k=200
print(i,j,k)
a,b=100,200
print(a,b)
a=100
b=200
a=b
b=a
print(a,b)
a=100
b=200
temp=a
a=b
b=temp
print(a,b)
a=100
b=200
a,b=b,a
print(a,b)
#3-2-2
a=10
a+=2
a*=5
a//=3
a%=6
print(a)
#3-3
s=eval(input('please enter an integer:'))
print(s)
s2=input('please enter a string:')
print(s2)
str2=input('please enter an integer:')
num=int(str2)+100
str2=eval(input('please enter an integer:'))
num=str2+100
print(num)
num1=eval(input('please enter number1:'))
num2=eval(input('please enter number2:'))
print(num1+num2)
num1,mun2=eval(input('please enter tow number separated by comma:'))
print(num1+num2)
#3-4
num1,num2,num3=eval(input('enter three number separated by comma:'))
print('total=',num1+num2+num3)               
print('average=',(num1+num2+num3)/3)
radius=eval(input('enter the radius:'))
print('area=',radius*radius*3.14159)
print('perimeter=',2*radius*3.14159)
import math
radius=eval(input('enter the radius:'))
print('area=',radius*radius*math.pi)
print('perimeter=',2*radius*math.pi)
#3-5
'''
this prigram display learning python now!
and python is fun
'''

