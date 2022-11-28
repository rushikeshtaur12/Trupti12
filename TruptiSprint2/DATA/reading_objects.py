import xlrd
# path=r"C:\Users\Trupti\Desktop\nov16.xlsx"
from LIBRARY.config import Config
###################################################
def read_locators():
    workbook= xlrd.open_workbook(Config.Data_path)
    worksheet= workbook.sheet_by_name("flightSearch")
    row=worksheet.nrows   #reads the data and returns the generator object
    # print(rows)
    d={}
    for i in range(row):
        row=worksheet.row_values(i)
        print(row)
        d[row[0]] = (row[1],row[2])
    return d

print(read_locators())

def read_data():
    workbook = xlrd.open_workbook(Config.Data_path)
    worksheet = workbook.sheet_by_name("data")
    row = worksheet.get_rows() # reads the data and returns the generator object
    columns=worksheet.ncols
    header=next(row)
    data = []
    for rows in row:
        values=()
        for j in range(columns):
            values+=(rows[j].value,)
        data.append(values)

    return data


