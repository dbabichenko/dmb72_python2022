import json

f = open('diabetes.csv')
data = f.readlines()
dataset = []
for row in data[1:]:
    row_values = row.split(",")
    temp = {
        "id" : row_values[0].strip(),
        "chol" : row_values[1].strip(),
        "stab.glu" : row_values[2].strip(),
        "hdl" : row_values[3].strip(),
        "ratio" : row_values[4].strip(),
        "glyhb" : row_values[5].strip(),
        "location" : row_values[6].strip(),
        "age" : row_values[7].strip(),
        "gender" : row_values[8].strip(),
        "height" : row_values[9].strip(),
        "weight" : row_values[10].strip(),
        "frame" : row_values[11].strip(),
        "bp.1s" : row_values[12].strip(),
        "bp.1d" : row_values[13].strip(),
        "waist" : row_values[14].strip(),
        "hip" : row_values[15].strip()
    }
    dataset.append(temp)

print(json.dumps(dataset[:10]))