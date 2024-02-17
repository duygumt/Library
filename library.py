#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 13:44:46 2024

@author: duygumetin
"""

class Library:
    def __init__(self,file_name ="books.txt" ):
        self.file_name = file_name
        self.file = open(self.file_name, "a+")
    def __del__(self):
        self.file.close()
    def list_books(self):
        lines = self.file.read().splitlines()
        for line in lines:
            kitap = line.split(",")
            if len(kitap) == 2:
                book_name , author = kitap
                print("Book" + book_name + ",Author" + author)
            else:
                print("Cannot found any data")
    def add_book(self):
        book_title = input("Book title:")
        book_author = input("Book author:")
        release_year = input("Release year:")
        number_of_pages = input("Number of pages:")
        total = f"{book_title.strip()}, {book_author.strip()}, {release_year.strip()}, {number_of_pages.strip()}\n" 
        self.file.write(total)
    def remove_book(self):
        remove = input("Book title:")
        lines = self.file.read().splitlines()
        removed =[]
        for removed in lines:
            lines.index(remove)
        self.file.truncate()
        for book in removed:
            self.file.write(book + "\n")
lib = Library()
print("***  MENU  ***" )
print("1)List Books")
print("2)Add Book")
print("3)Remove Book")

user_preference = input("Choose one option:")
if user_preference == "1":
    lib.list_books()
elif user_preference == "2":
    lib.add_book()
elif user_preference == "3":
    lib.remove_book()
else:
    print("You cannot choose a number except 1,2,3")

    

    


            
        
        
        
            
        
        
        
                
                
        
        
    
        
        
        
   