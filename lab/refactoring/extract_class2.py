movies = [['Tenet', 'Vita & Virgina', 'Guardians of the Galaxy', 'The Great Gatsby'],\
     ['Ace Ventura', 'The Mask', 'Dumb and Dumber', 'The Truman Show', 'Yes Man']]
class PersonalInfo:
    def __init__(self):
        self.first_names = ['elizabeth', 'Jim']
        self.last_names = ['debicki', 'Carrey']
        self.birth_year = [1990, 1962]
        self.emails = ['deb@makeschool.com', 'jim@makeschool.com']

    def send_hiring_email(email):
        print("email sent to: ", self.email)
        
    def is_millennial(birth_year):
        for i, value in enumerate(emails):
            if self.birth_year[i] > 1985:
                print(self.first_names[i], self.last_names[i])
                print('Movies Played: ', end='')
                for m in movies[i]:
                    print(m, end=', ')
                print()
                send_hiring_email(value)