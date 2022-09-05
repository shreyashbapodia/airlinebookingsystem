# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 

@author: Shreyash Bapodia
"""
def book_seat(flights):
    
    print("\nList of all available flights")
    for i,item in enumerate(flights):
        print(i+1,"Model = " + item._model + ", Total Seats Available =",item._num_seats_left)
        
    print("\nSelect index to book a seat")
    index = int(input())
    
    if(index<1 or index > len(flights)):
        print("\nInvalid Index")
        return
    
    if(flights[index-1]._num_seats_left <=0 ):
        print("\nNo seats available try again")
        return
    
    flights[index-1].seats()
    
    print("\nEnter row")
    row = int(input())
    row = row-1
    print("\nEnter seat")
    seat = input()
    print("\nEnter name")
    name = input()
    
    if(flights[index-1]._seats[row][seat]!=None):
        print("\nAlready Booked! Try Again")
        return
    
    flights[index-1]._seats[row][seat] = name
    flights[index-1]._num_seats_left = flights[index-1]._num_seats_left -1      
    flights[index-1].seats()
    print("\n Seat Booked Successfully")
    return
    