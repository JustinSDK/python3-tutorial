import pickle

class DVD:
    def __init__(self, title, year=None, duration=None, director_id=None):
        self.title = title
        self.year = year
        self.duration = duration
        self.director_id = director_id
        self.filename = self.title.replace(' ', '_') + '.pkl'

    def check_filename(self, filename):
        if filename is not None:
            self.filename = filename

    def save(self, filename=None):
        self.check_filename(filename)

        fh = None
        try:
            data = (self.title, self.year, self.duration, self.director_id)
            with open(self.filename, 'wb') as fh:
                pickle.dump(data, fh)
        except (EnvironmentError, pickle.PicklingError) as err:
            raise SaveError(str(err))

    def load(self, filename=None):
        self.check_filename(filename)

        fh = None
        try:
            with open(self.filename, 'rb') as fh:
                data = pickle.load(fh)
                (self.title, self.year, self.duration, self.director_id) = data
        except (EnvironmentError, pickle.PicklingError) as err:
            raise LoadError(str(err))

    def __str__(self):
        return 'DVD({0}, {1}, {2}, {3})'.format(
            self.title, self.year, self.duration, self.director_id)

def main():
    dvd1 = DVD('Python 3 Tutorial', 2016, 1, 'Justin Lin')
    dvd1.save()
    dvd2 = DVD('Python 3 Tutorial')
    dvd2.load()
    print(dvd2)
    

if __name__ == '__main__':
    main()
