import xlrd
filename = "G:\\2017dianshang3.sql"
wb = xlrd.open_workbook(r"G:\biaodan\Class3.xlsx")
sh = wb.sheet_by_index(0)  # 第一个表
colName = sh.col_values(0)#读取一列的数据
def source():
    for col in range(1,len(colName)):
        rowName = sh.row_values(col)
        sex = rowName[2]
        Tel = str(int(rowName[6]))
        identity = rowName[7]
        stuNo = int(rowName[1])
        writer(sex,Tel,identity,stuNo)
def writer(sex,Tel,identity,stuNo):
    if sex =="男":
        sex = 1
    else:
        sex = 0
    SQL = "update b_userinfo set gender = %s,telephone = '%s',others='{\"identity\":\"%s\"}' where studentid = '%s'"%(sex,Tel,identity,stuNo)
    SQLS = SQL+";"
    print(SQL+";")
    with open(filename,'a',encoding='utf-8') as f: # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
        f.write(SQLS)
        f.close()
if __name__ == '__main__':
    source()
#sdadas 