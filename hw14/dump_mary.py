import pickle

from hw14.employee import Employee


if __name__ == '__main__':
    mary = Employee("Mary", 25)

    with open('mary.pickle', 'wb') as f:
        pickle.dump(mary, f)
