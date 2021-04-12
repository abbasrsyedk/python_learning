#
#
#

class Book():

    def __init__(self,title,author,pages):

        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return self.title + " by "+  self.author + " with a total of " +self.pages + " pages"
    
    def __len__(self):
        print("A book object has been deleted")

b = Book('python', 'abbas', '200')

#print(b)
print(b)


