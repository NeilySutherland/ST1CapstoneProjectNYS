# Week 9 Challenge problem A & B

#Set class
class LibraryItem:
    def __init__(self, item_name, author, publisher):
        self.item_name = item_name
        self.author = author
        self.publisher = publisher

#Set superclass
class Book(LibraryItem):
    def __init__(self, item_name, author, publisher, title, num_pages, has_hard_copy, has_ebook):
        super().__init__(item_name, author, publisher)
        self.title = title
        self.num_pages = num_pages
        self.has_hard_copy = has_hard_copy
        self.has_ebook = has_ebook

    #Mutators
    def set_item_name(self, item_name):
        self.item_name = item_name

    def set_author(self, author):
        self.author = author

    def set_publisher(self, publisher):
        self.publisher = publisher

    def set_title(self, title):
        self.title = title

    def set_num_pages(self, num_pages):
        self.num_pages = num_pages

    def set_hard_copy(self, has_hard_copy):
        self.has_hard_copy = has_hard_copy

    def set_ebook(self, has_ebook):
        self.has_ebook = has_ebook

    #Accessors
    def get_item_name(self):
        return self.item_name
    
    def get_author(self):
        return self.author
    
    def get_publisher(self):
        return self.publisher
    
    def get_title(self):
        return self.title
    
    def get_num_pages(self):
        return self.num_pages
    
    def has_hard_copy(self):
        return self.has_hard_copy
    
    def has_ebook(self):
        return self.has_ebook
    
    #Ebook and Hard copy...?
    def ebook_and_hard_copy(self):
        if self.has_hard_copy == True and self.has_ebook == True:
            self.ebook_and_hard_copy == True
        else:
            self.ebook_and_hard_copy == False


#Tester
if __name__ == "__main__":
    #Book examples
    book1 = Book("Book 1", "Hashimoto", "ST1 inc.", "Caps in stones", 18, True, False)
    book2 = Book("Book 2", "Gregory", "Gregory gigs", "Life of Gregory", 246, True, True)
    book3 = Book("Book 3", "Mikasa", "Baldwin's boldness", "Attack on big boy", 567, False, False)

    #Print Examples
    print("Item name:", book1.get_item_name())
    print("Author:", book1.get_author())
    print("Publisher:", book1.get_publisher())
    print("Book title:", book1.get_title())
    print("Number of Pages:", book1.get_num_pages())
    print("Has Hard Copy:", book1.has_hard_copy)
    print("Has eBook:", book1.has_ebook)
    print("Has ebook and hard copy:", book1.ebook_and_hard_copy())
    print("\n")
    print("Item name:", book2.get_item_name())
    print("Author:", book2.get_author())
    print("Publisher:", book2.get_publisher())
    print("Book title:", book2.get_title())
    print("Number of Pages:", book2.get_num_pages())
    print("Has Hard Copy:", book2.has_hard_copy)
    print("Has eBook:", book2.has_ebook)
    print("Has ebook and hard copy:", book2.ebook_and_hard_copy())
    print("\n")
    print("Item name:", book3.get_item_name())
    print("Author:", book3.get_author())
    print("Publisher:", book3.get_publisher())
    print("Book title:", book3.get_title())
    print("Number of Pages:", book3.get_num_pages())
    print("Has Hard Copy:", book3.has_hard_copy)
    print("Has eBook:", book3.has_ebook)
    print("Has ebook and hard copy:", book3.ebook_and_hard_copy())