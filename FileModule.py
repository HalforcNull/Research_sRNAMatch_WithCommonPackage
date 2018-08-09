import csv

def __LoadCSVData(fileName, isNumericData = True, removeEmpty = True):
    data = []
    with open(fileName, 'rt') as csvfile:
        datas = csv.reader(csvfile, delimiter = ',')
        for row in datas:
            if removeEmpty and ( row is None or len(row) == 0 ):
                continue
            if isNumericData:
                data.append(map(float,row))
    return data