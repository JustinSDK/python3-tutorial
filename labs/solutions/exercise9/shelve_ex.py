import shelve

class DVD:
    def __init__(self, title, year=None, duration=None, director_id=None):
        self.title = title
        self.year = year
        self.duration = duration
        self.director_id = director_id

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return 'DVD({0}, {1}, {2}, {3})'.format(
            self.title, self.year, self.duration, self.director_id)

class DvdDao:
    def __init__(self, shelve_name):
        self.shelve_name = shelve_name

    def save(self, dvd):
        shelve_db = None
        with shelve.open(self.shelve_name) as shelve_db:
            shelve_db[dvd.title] = (dvd.year, dvd.duration, dvd.director_id)
            shelve_db.sync()

    def all(self):
        shelve_db = None
        with shelve.open(self.shelve_name) as shelve_db:
            shelve_db = shelve.open(self.shelve_name)
            return [DVD(title, *shelve_db[title]) 
                    for title in sorted(shelve_db, key=str.lower)]
        return []

    def load(self, title):
        with shelve.open(self.shelve_name) as shelve_db:
            if title in shelve_db:
                return DVD(title, *shelve_db[title])
        return None

    def remove(self, title):
        with shelve.open(self.shelve_name) as shelve_db:
            del shelve_db[title]
            shelve_db.sync()

def main():
    filename = 'dvd_library.slv'
    dao = DvdDao(filename)
    dvd1 = DVD('Python 2 Tutorial', 2013, 1, 'Justin Lin')
    dvd2 = DVD('Python 3 Tutorial', 2016, 1, 'Justin Lin')
    dao.save(dvd1)
    dao.save(dvd2)
    print(dao.all())
    print(dao.load('Python 2 Tutorial'))
    dao.remove('Python 3 Tutorial')
    print(dao.all())


if __name__ == '__main__':
    main()
