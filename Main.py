# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 12:57:10 2019

@author: github.com/salmalfarisi/
"""

#add total score from user input
def add(x, y):
    return x + y

#decrease total score from user input
def minus(x, y):
    return x - y

#multiply total score from user input
def multiply(x, y):
    return x * y

#divide total score from user input
def divide(x, y):
    return x / y

#main program
def main(recent): 
    print("Basic Calculator")
    print("Select Operation : ")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Reset Program")
    print("6. Exit")
    print("")
    
    #save last score operation    
    if recent != "":
        print("Temp Score =", recent)
    else:
        print("No Recent Score to save in this Program")
    #user input for choice
    choice = input("Your Option : ")

    #if user choose add operation
    if choice == '1':
        print("Add Operation")
        if recent != "":
            print("First Input : ", recent)
            int1 = recent
        else:
            int1 = int(input("First Input : "))
        int2 = int(input("Second Input : "))
    #if user choose subtract operation
    elif choice == '2':
        if recent != "":
            print("First Input : ", recent)
            int1 = recent
        else:
            int1 = int(input("First Input : "))
        int2 = int(input("Second Input : "))
    #if user choose multiply operation
    elif choice == '3':
        print("Multiply Operation")
        if recent != "":
            print("First Input : ", recent)
            int1 = recent
        else:
            int1 = int(input("First Input : "))
        int2 = int(input("Second Input : "))
    #if user choose divide operation
    elif choice == '4':
        if recent != "":
            print("First Input : ", recent)
            int1 = recent
        else:
            int1 = int(input("First Input : "))
        int2 = int(input("Second Input : "))
    #if user choose to reset recent history
    elif choice == '5':
        print("")
        print("Successfully Reset Program")
        print("")
        recent = ""
        main(recent)
    #if user choose try to exit from program
    elif choice == '6':
        print("")
        print("Success to Exit from Program!!")
        print("")
    #if user choose wrong input
    else:
        print("")
        print("Sorry, wrong input. Try again")
        print("")
        recent = ""
        main(recent)
    
    #if user choose add operation
    if choice == '1':
        print(int1, "+", int2, "=", add(int1,int2))
        print("Recent History : ", int1, "+", int2, "=", add(int1,int2))
        recent = add(int1, int2)
        main(recent)
    #if user choose subtract operation
    elif choice == '2':
        print(int1, "-", int2, "=", minus(int1,int2))
        print("Recent History : ", int1, "-", int2, "=", minus(int1,int2))
        recent = minus(int1, int2)
        main(recent)
    #if user choose multiply operation
    elif choice == '3':
        print(int1, "*", int2, "=", multiply(int1,int2))
        print("Recent History : ", int1, "*", int2, "=", multiply(int1,int2))
        recent = multiply(int1, int2)
        main(recent)
    #if user choose divide operation
    elif choice == '4':
        print(int1, "/", int2, "=", divide(int1,int2))
        print("Recent History : ", int1, "/", int2, "=", divide(int1,int2))
        recent = divide(int1, int2)
        main(recent)        

recent = ""
main(recent)