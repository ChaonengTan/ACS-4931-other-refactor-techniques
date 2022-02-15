# by Kami Bigdely
# Extract class
first_names = ['elizabeth', 'Jim']
last_names = ['debicki', 'Carrey']
birth_year = [1990, 1962]
movies = [['Tenet', 'Vita & Virgina', 'Guardians of the Galexy', 'The Great Gatsby'],\
     ['Ace Ventura', 'The Mask', 'Dubm and Dumber', 'The Truman Show', 'Yes Man']]
emails = ['deb@makeschool.com', 'jim@makeschool.com']

class Actor:
    def __init__(self, firstName, lastName, birthYear, movies, email):
        self.firstName = firstName
        self.lastName = lastName
        self.birthYear = birthYear
        self.movies = movies
        self.email = email

    def sendHiringEmail(self, email):
        print(f"email sent to: {email}" )

    def bornAfter1985(self):
        if self.birthYear > 1985:
            print(f"{self.firstName} {self.lastName}")
            print('Movies Played: ', end='')
            for m in self.movies:
                print(m, end=', ')
            self.sendHiringEmail(self.email)
        else:
            print("Born before 1985")

elizabeth = Actor('Elizabeth', 'Debicki', 1990, ['Tenet', 'Vita & Virgina', 'Guardians of the Galexy', 'The Great Gatsby'], 'deb@makeschool.com')
jim = Actor('Jim', 'Carrey', 1962, ['Ace Ventura', 'The Mask', 'Dubm and Dumber', 'The Truman Show', 'Yes Man'], 'jim@makeschool.com')

elizabeth.bornAfter1985()
jim.bornAfter1985()