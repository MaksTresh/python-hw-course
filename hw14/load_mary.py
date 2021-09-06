import pickle

from hw14.employee import Employee


if __name__ == '__main__':
    with open('mary.pickle', 'rb') as f:
        mary = pickle.load(f)

    print(mary)
