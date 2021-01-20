class Author:
    def __init__(self, name): #self is constant and never change.
        self.name = name
        self.books = []

    def published(self, title):
            if title in self.books:
                print('The title already exist')
            else:    
                self.books.append(title) #this method is used to add items to the list

    def __str__(self):
        book_list=', '.join(self.books) #joins all items using ,
        return f'Name of the author is : {self.name}  and the books are: {book_list}'
def main():        

    shakspeare = Author('William Shakspeare')
    shakspeare.published('Halmet')
    shakspeare.published('Richard II')
    shakspeare.published('Halmet')

    print(shakspeare)
if __name__ == "__main__":
    main()    




