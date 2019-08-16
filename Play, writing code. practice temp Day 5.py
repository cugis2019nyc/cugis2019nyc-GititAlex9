# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 11:25:42 2019

@author: columbia
"""

print("hello world, 10 divided by 5 equals") 
print(10/5)
print("Answer")
print("I am learning to code, 100 divided by 3 is")
print(100/3)

print("Grand Answer isss.............. 5 times 4 is")
print(5*4)

print("5+4=")
print(5+4)

print("5-1=")
print(5-1)

print(5**2) #squaring
print((5*6)/3)

def add(a,b):
    add = a+b
    print(add)
add(5555.5,105555)

def adds(a,b,c):
    adds = a+b+c
    print("The sum of",a,",",b,"and",c,"='s",adds)
    
def multiply(a,b):
    multiply = a*b
    print(multiply)
multiply(5,5)

def bh(a,b):
    bh = a*b*1/2
    print("The area of this triangle is",bh)
bh(5,8)

def trapezoid(a,b,h):
    trapezoid = ((a+b)/2)*h
    print("Base, base, height")
    print("Trapezoid area is",trapezoid)
trapezoid(4,8,2)

def circle(a):
    circle = ((3.1415926*a)**2)
    print("Pi, radi, squared, plug in radius")
    print("Circle area is",circle)
circle(2)

import math
dir(math)
math.factorial(7)
math.sqrt(350)
math.exp(2)
pow
math.pow(2.718281828459045,2)
math.pow(35,9)
35**9
math.pi

chocolate1 = "milk"
chocolate2 = "dark"
chocolate3 = "white"
milk = 5
dark = 4
white = 9
#milk = milk+3

#dark = dark**3

print(milk-2)

#Dict

chocolate1 = {"milk":5}
chocolate2 = {"dark":4}
chocolate3 = {"white":9}
chocolatebox = [{"white":9, "milk":5, "dark":4}]
print("In the box there are", chocolatebox)
#chocolatebox
#[list]{dict}

#chocolate_box = [chocolate1,chocolate2,chocolate3]
#chocolate_box = input("Chocolate box flavors are",chocolate_box)
#print(chocolate_box)

cat = 3
dog = 1
bird = 2
petbox = [{cat, dog, bird}]
petbox


import pandas
dir(pandas)
student1 = ["Henrik",32,"M"]
student2 = ["Troy",50,"M"]
student3 = ["Lexi",30,"F"]
student4 = ["Caleb",40,"M"]
print(student1, student2, student3, student4)
students = [student1, student2, student3, student4]
students
studentinfo = [["Henrik",32,"M"],["Troy",50,"M"],["Lexi",30,"F"],["Caleb",40,"M"]]
studentdf = pandas.DataFrame(studentinfo,columns=("name","scores","gender"))
studentdf
studentdf["name"]
studentdf["scores"]
studentdf["gender"]
import pandas
dir(pandas)

import plotly
dir(plotly)

from plotly.offline import plot
import plotly.graph_objs as go

studentbar = go.Bar(x=studentdf["name"], y = studentdf["scores"])
plot([studentbar])
studentbar


wodf = pandas.read_excel("GISdata.xlsx",sheet_name = "womenOccupation")
wodf =  pandas.read_excel("GISdata.xlsx", sheet_name = "womenOccupation")
womenOccupation = go.Bar(x=wodf["occupation"], y=wodf["women"],
                         marker = {"color": wodf["women"],
                                   "colorscale" : "rainbow"})
titles = go.Layout(title = "Percentage of Women Emplyed by Occupation",
                   xaxis=go.layout.XAxis(title=go.layout.xaxis.Title(text="Occupation",
                                                                     )
                                                                    ),
    
    yaxis=go.layout.YAxis(title=go.layout.yaxis.Title(text="Percentage",
                                                  )
                                                ),
    )

    
    #https://community.plot.ly/t/what-colorscales-are-available-in-plotly-and-which-are-the-default/2079/2
#agename = go.Bar(x=studentlistdf["name"], y=studentlistdf["scores"])
#plot([agename])
                   
import pandas
dir(pandas)


Choco1 = ["Milk",5]
Choco2 = ["Dark",6 ]
Choco3 = ["White",8]
print(Choco1, Choco2, Choco3)
chocolates = [Choco1, Choco2, Choco3]

chocolateinfo = [["Milk",5],["Dark",6],["White",8]]
chocolatesdf = pandas.DataFrame(chocolates,columns=("Type","Quanity"))
chocolatesdf

chocolatesdf["Type"]




#greet a person by  their name
print("Hello Alex")
a ="Alex"
print("Hello",a)    

name = input 

#def NameOfFunction(parameters)



import pandas
dir(pandas)

import plotly
dir(plotly)

from plotly.offline import plot
import plotly.graph_objs as go


cdf =  pandas.read_excel("GISdata.xlsx", sheet_name = "cancercases")
cancercases = go.Bar(x=cdf["CancerType"], y=cdf["Number"],
                         marker = {"color": cdf["Number"],
                                   "colorscale" : "jet"})
titles = go.Layout(title = "Percentage of cancercases",
                   xaxis=go.layout.XAxis(title=go.layout.xaxis.Title(text="Years",
                                                                     )
                                                                    ),
    
    yaxis=go.layout.YAxis(title=go.layout.yaxis.Title(text="Percentage",
                                                  )
                                                ),
    )








#if (5+4) is (9) 
#print("correct")
#path = '9'
#if path:('9')
#    print "True"
#else:
 #   print "False"
    