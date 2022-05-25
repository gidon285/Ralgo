import gspread
import numpy as np


account = gspread.service_account("C:\\Users\\gidon\\OneDrive\\Desktop\\Ralgo\\HM6\\algorithmsq2-1a1003d9fd9d.json")
spreadsheet = account.open("test")
sheet1 = spreadsheet.worksheet("Sheet1")

# A1 always contains the number of matrix to multiply, thus we create the list that will contain the matrixes.
t_arr ,arr ,mult = [], [], []
num_of_col = int(sheet1.acell("A1").value)+1
num_of_row = int(sheet1.acell("A2").value)+1

for i in range(1,num_of_col):
    for j in range(2,num_of_row):
        string = str(sheet1.cell(i, j).value).replace("[","").replace("]","").split(",")
        if string is not None:
            for num in string:
                t_arr.append(int(num))
            arr.append(t_arr)
            t_arr = []
    mult.append(arr)
    arr = []


a = np.array([mult[0],mult[1]])
b = np.array([mult[3],mult[4]])

sheet1.update("A2", str(np.matmul(a,b)))