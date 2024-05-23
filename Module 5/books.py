
def booksScore(num_books):
    points = 0
    if num_books == 0:
        points = 0
    elif num_books >= 2 and num_books < 4:
        points = 5
    elif num_books >= 4 and num_books < 6:
        points = 15
    elif num_books >= 6 and num_books < 8:
        points = 30
    elif num_books >= 8:
        points = 60
    return points
    
if __name__ == "__main__":
    books_purchased = int(input("Enter the amount of books purchased this month: "))
    score = booksScore(books_purchased)
    print("{} points awarded!".format(score))