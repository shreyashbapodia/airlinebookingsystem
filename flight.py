# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 

@author: Shreyash Bapodia
"""
from pprint import pprint as pp

class Flight:
        
    def __init__ (self, model, num_rows, num_seats_per_row):
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row
        self._num_seats_left = num_rows*num_seats_per_row
        self.s = "ABCDEFGH"
        self._seats = []
        
        for i in range(0,self._num_rows):
            _temp_row = {}
            
            for j in range(0,self._num_seats_per_row):
                _temp_row[self.s[j]] = None
                
            self._seats.append(_temp_row)
                
               
    def info(self):
        print("\nModel = " + self._model)
        print("Total Seats Available =",self._num_seats_left)
        
    def seats(self):
        print("")
        pp(self._seats)
       
def create_flight():
    
    print("\nEnter Model")
    model = input()
    print("\nEnter Total Rows")
    num_rows = int(input())
    print("\nEnter Seats per Row")
    num_seats_per_row = int(input())
    
    f = Flight(model,num_rows,num_seats_per_row)
    
    return f

def show_flights(flights):
 
    print("\nList of all available flights")
    for i,item in enumerate(flights):
        print(i+1,"Model = " + item._model + ", Total Seats Available =",item._num_seats_left)
        
    print("\nSelect index to show seating plan")
    index = int(input())
    
    if(index>0 and index<=len(flights)):
        flights[index-1].seats()
        

    
    

    