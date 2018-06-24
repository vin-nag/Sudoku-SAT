import pickle

class Reducer():

    def __init__(self, path='output'):
        self.path = path

    def get_cnf_data(self, cnf_path='sudoku9.cnf'):
        with open(cnf_path) as f:
            cnf=f.readlines()
        print(cnf)

    def create_cnf_file(self):
        with open(self.path, 'rb') as fp:
            itemlist = pickle.load(fp)

        print(itemlist)

