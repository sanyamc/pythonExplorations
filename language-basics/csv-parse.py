import csv


def load_file(filename, types, error='error'):
    '''
        returns the types zipped with data
    '''

    if error not in ['error', 'silent']:
        raise ValueError

    with open(filename, 'r') as file:
        lines = []
        row = csv.reader(file)
        for rowno, row in enumerate(row):
            try:
                row = [func(val) for func, val in zip(types, row)]
                print(row)
                lines.append(row)
            except ValueError as e:
                if error == 'error':
                    print('Bad rowno: {}'.format(rowno))
                    print('error: {}'.format(e))
                continue
        return lines


if __name__ == '__main__':
    load_file('samplecsv.csv', [int,str,str,str,str,str,str,str,str,str,str,str,str])
