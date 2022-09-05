# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 

@author: Shreyash Bapodia
"""
from flight import *
from booking import *

flights = []

while(1):
    
   print("\nFLIGHT BOOKING SYSTEM")
   print("\n1. Create a new Flight")
   print("2. Show all Flights")
   print("3. Book a seat")
   print("0. Exit")
        
   text = input()
   if(text=='0'):
       break
   
   if(text=='1'):
       f = create_flight()
       flights.append(f)
       f.info()
       f.seats()
   
   if(text=='2'):
       show_flights(flights)
   
   if(text=='3'):
       book_seat(flights)
            
        
        
        
    