'''Library program

1. Display books - done
2. Lend books  - done
3. Donate books - done
4. Return books


'''
import time

class Library :
    rent_records = {}
    donated = {}
    
    # Books that are in the library whether issued or not.
    all_books = {}
    
    def __init__(self,books:list,lib_name):
        self.lib_name = lib_name
        self.book_list = books
        self.books = {}
        self.__class__.all_books = self.books
        
        _ = list(map(lambda serial, book : self.books.update({serial:book}),range(1,len(books)+1), books ))
        
        print('\n',time.asctime(time.localtime()))
        
        welcome = f"Welcome to \'{self.lib_name}\' Library"
        print(f'\n{welcome:`^80}\n')
        
        self.is_book_available = lambda x : True if x!=[] else False
    
    # Main Event Loop
    def user_entry(self):
        self.user_name = input("Enter your user name : ")
        
        # IF username is empty the call this function again .
        if self.user_name.strip() == '':
            self.user_entry()
            
        time.sleep(1)
        print("Logged in...\n")
        time.sleep(1)
        
        
        while True :
            available = (lambda x : '' if self.is_book_available(self.book_list) else '{ Not available }')('x')

            user_functions = "\n|> You can - \n.Display Available Books - 1"\
            f"\n.Rent Books   - 2 {available}\n.Donate Books - 3\n.Return Books - 4\n"
            
            self.line_break()
            print(user_functions)
            self.line_break()
            
            user_choice = input("What do you want to do ? : ")
            
            while not user_choice.isnumeric():
                print("Input Error")
                self.line_break()
                user_choice = input("What do you want to do ? : ")
                if user_choice.isnumeric():
                    break
                elif user_choice.lower().strip() == 'exit':
                    print("Exit Requested...")
                    time.sleep(1)
                    print("Exit Successful!")
                    quit()
                    
            user_choice = int(user_choice)
               
            # To display all the available books
            if user_choice == 1:
                self.display_books()
            
            # For lending books   
            elif user_choice == 2:
                
                self.lend_book(self.user_name)
                
            # For donating books
            elif user_choice == 3:
                self.donate_book()
                
            # For returning book
            elif user_choice == 4:
                if not self.user_name in self.rent_records.keys():
                    print("Please issue some books first...")
                    time.sleep(1)
                    continue
                
                self.return_books_checker(self.user_name)
                 

                
                
    @staticmethod
    def line_break():
        print(f"{'=':=^50}")
        
        
    def display_books(self):
        
        if self.books == {}:
            print("Sorry, we don't have any book available, you can donate one..."\
                "\nWe are sorry for the inconvenience.")
        
        print("\nWe have the following books in library :-")
        for index,book in self.__class__.all_books.items():
            print(f"{index}. {book}")

        
        self.line_break()
        time.sleep(2)
    
    def lend_book(self,user_name):
        print(f'\n{"You Have Chosen To Rent Books":=^50} ')
        self.display_books()
        
        book_serials = input("Enter your book's serial no.\n"\
        "If you want more than one book, then enter their serial numbers separated by comma.\n : ").split(',')
        
        rent_these_books = []
        
        book_serials = list(map(lambda x : int(x.strip()),book_serials))
        
        filtered_book_serials = list(filter(lambda x : x in self.books.keys(), book_serials))
        
        errors = list(set(book_serials).difference(filtered_book_serials))
        not_in_stock = []
        
        for serial in filtered_book_serials:
            serial = serial
            
            if self.books[serial] in self.book_list:
                rent_these_books.append( self.books[serial] )
            else:
                not_in_stock.append(self.books[serial])
            
        if user_name in self.rent_records:
            self.__class__.rent_records[user_name].append(rent_these_books)
        else:
            self.__class__.rent_records[user_name] = rent_these_books
        
        for item in rent_these_books:
            self.book_list.remove(item)
        
        if errors:
            print(f"Errors for the serial no. {errors}")
            time.sleep(1)
                        
        elif len(errors) == len(book_serials):
            print("Errors in issuing books.. No book issued. Enter a valid serial no.")
            time.sleep(1)
            
            
        elif rent_these_books != []:
            print(f"Successfully Issued books ! {rent_these_books} ")
            time.sleep(1)
        
        elif not_in_stock :
            if rent_these_books == []:
                print("Sorry !! :(")
                time.sleep(0.6)
                print("The book has already been issued by someone,")
                time.sleep(3)
            else:
                print("Books Which Were already issued by someone are - ")
            
            for item in not_in_stock:
                for person,book in self.rent_records.items():
                    if item in book:
                        print(f"{item} - {person}")
        time.sleep(1)
     
        
        
    #Method for donating books
    def donate_book(self):
        print(f'\n{"You Have Chosen To Donate Books":=^50} ')
        print("Enter the name(s) of books one by one and \ntype 'finish' - to finish it"\
            "\ntype 'del prev' - to delete the previous entry.\n")
        time.sleep(1)
        
        new_books = []
        counter = 1
        
        while True:
            dbook_name = input(f"Enter Book Name ({counter}). - ")
            dbook = dbook_name.lower().strip()
            
            
            if dbook == 'finish':
                break
            
            elif dbook == 'del prev' and len(new_books) != 0:
                print("Counter value - ", counter)
                del new_books[counter-2]
                counter -= 1
            
            elif dbook == 'del prev' and len(new_books) == 0:
                print("Please Enter a Book Name First ...")
                counter-=1
                
            else:
                new_books.append(dbook_name)
                counter += 1
        
        stock_books = list(self.books.values())
        
        new_books = list(filter(lambda x : not x in stock_books, new_books ))
        new_books_list = [ stock_books.append(i) for i in new_books]
        print(new_books,stock_books)
        
        print("\nSucessfully Donated Books!! Thank You for donating :)")
        self.line_break()
        time.sleep(1) 
        self.__init__(stock_books, self.lib_name)
        
        
        
        
    
    #Method of returning books
    def return_books(self,user_name,book_index):
        rented_books = self.rent_records[self.user_name]
        
        if len(rented_books) == 1:
            del self.rent_records[user_name]
        else:
            del rented_books[book_index - 1]
            self.__class__.rent_records[user_name] = rented_books
            
        self.book_list.append(self.books[book_index])
        print(f"Successfully returned book [{self.books[book_index]}]...")
        time.sleep(1)
       
    
    def return_books_checker(self,user_name):
        rented_books = self.rent_records[self.user_name]
        rented_books_dict = {}
        _ = list(map(lambda serial,book_name : rented_books_dict.update({serial:book_name}), 
                        range(1,len(rented_books)+1), rented_books) )
        self.line_break()
        print("Issued Books are : - ")
        for serial,book in rented_books_dict.items():
            print(f'{serial}. {book}')
            
        while True:
            return_book = input("Enter the serial of book to be returned : ")
            if return_book.isnumeric() and int(return_book) in rented_books_dict.keys():
                return_book = int(return_book)
                break
            
        self.return_books(self.user_name,return_book)
                        
        
        
        
books = ["Harry Potter", "NCERT Physics", "Core Python By Nageshwar Rao",'Twinkle','Let us C','Core Java']
kalaLib = Library(books,'KaladharLib')


kalaLib.user_entry()
        
    

