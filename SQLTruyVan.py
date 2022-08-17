
import sqlite3

class truyVanSQL():

    def select(self, conn):
        for row in cursor:
            print("ID = ", row[0])
            print("NAME = ", row[1])

    def ketNoi(self, conn):
        try:
            conn = sqlite3.connect('db.sqlite3')
            print("Kết nối database thành công")
        except Exception as e:
            print("Kết nối database thất bại")
            print(e)
        return conn

    def laySoLuongBanGhiCuaBang(self, conn,name_table,name_column):
        chuoiLaySL="SELECT count(*) FROM "+name_table+" WHERE "+name_column+" IS NULL UNION ALL SELECT count(*) FROM "+name_table+" WHERE "+name_column+" IS NOT NULL"
        print(chuoiLaySL)
        cursor = conn.execute(chuoiLaySL)
        for row in cursor:
            return row[0]

    def boSung1BanGhiDuLieuVaoCSDL(self, conn, name_table, giaTriBoSung, cotCapNhat, soCot):
        temp1 = "INSERT INTO " + name_table + " "
        temp2 = " VALUES ('"
        temp3 = "')"
        chuoiCotCapNhat = "("
        for i in range(1, soCot + 1):
            chuoiCotCapNhat += cotCapNhat[i] + ","
        chuoiCotCapNhat = chuoiCotCapNhat[0:len(chuoiCotCapNhat) - 1:1] + ")"
        print(chuoiCotCapNhat)
        chuoiSQLBoSung = ""
        for i in range(1, soCot + 1):
            chuoiSQLBoSung += giaTriBoSung[i] + "','"
        chuoiSQLBoSung = temp1 + chuoiCotCapNhat + temp2 + chuoiSQLBoSung[0:len(chuoiSQLBoSung) - 3:1] + temp3
        print(chuoiSQLBoSung)
        conn.execute(chuoiSQLBoSung)
        conn.commit()

    def capNhat1GiaTriVao1CotCuaCSDL(self, conn, name_table, name_column, giatricapnhat):
        chuoiSQLCapNhat = "UPDATE " + name_table + " SET " + name_column + " = '" + giatricapnhat + "'"
        print(chuoiSQLCapNhat)
        conn.execute(chuoiSQLCapNhat)
        conn.commit()
    def capNhat1GiaTriVao1CotCuaCSDLVoiDieuKienID(self, conn, name_table, name_column, giatricapnhat,ID):
        chuoiSQLCapNhat = "UPDATE " + name_table + " SET " + name_column + " = '" + giatricapnhat + "' where id ="+str(ID)
        print(chuoiSQLCapNhat)
        conn.execute(chuoiSQLCapNhat)
        conn.commit()
    def taoBangNull(self, conn, name_table, name_column):
        chuoiSQLCapNhat = "UPDATE " + name_table + " SET " + name_column + " = NULL" 
        print(chuoiSQLCapNhat)
        conn.execute(chuoiSQLCapNhat)
        conn.commit()
    def xoaDongNull(self, conn, name_table, name_column):
        chuoiSQLXoa = 'delete from ' +name_table+ ' where '+ name_column +' IS NULL'
        print(chuoiSQLXoa)
        conn.execute(chuoiSQLXoa)
        conn.commit()
    def boSung1BanGhiNULLVaoCSDL(self, conn, name_table, cotCapNhat, soCot):
        temp1 = "INSERT INTO " + name_table + " "
        temp2 = " VALUES ("
        temp3 = ")"
        chuoiCotCapNhat = "("
        for i in range(1, soCot + 1):
            chuoiCotCapNhat += cotCapNhat[i] + ","
        chuoiCotCapNhat = chuoiCotCapNhat[0:len(chuoiCotCapNhat) - 1:1] + ")"
        print(chuoiCotCapNhat)
        chuoiSQLBoSung = ""
        for i in range(1, soCot + 1):
            chuoiSQLBoSung += "NULL,"
        chuoiSQLBoSung = temp1 + chuoiCotCapNhat + temp2 + chuoiSQLBoSung[0:len(chuoiSQLBoSung) - 1:1] + temp3
        print(chuoiSQLBoSung)
        conn.execute(chuoiSQLBoSung)
        conn.commit()
    def resetIndex(self, conn, name_table):
        chuoiSQLRESET="ALTER TABLE "+ name_table +" AUTO_INCREMENT=0"
        print(chuoiSQLRESET)
        #conn.execute(chuoiSQLRESET)
        #conn.commit()
        
    def layGiaTriDauTienTai1CotCuaCSDL(self, conn, name_table, name_column):
        chuoiSQLLayGiaTri="SELECT " + name_column + " FROM " + name_table
        print(chuoiSQLLayGiaTri)
        myresult = conn.execute(chuoiSQLLayGiaTri)
        a=None
        for x in myresult:
            a=x[0]
            break
        return a

a = truyVanSQL()
conn = None
conn = a.ketNoi(conn)


# 1)Form bổ sung 1 bản ghi (k cần thiết truyền vào đầy đủ các trường) vào 1 bảng SQL
# Bổ sung giá trị 5 Trường
with open('json.json','r',encoding='utf-8') as fileInp:
        chuoiOutputRaFile=None
        noiDungToanBoFile=fileInp.read()
giaTriCapNhat = [kteam for kteam in range(10)]
truongCapNhat = [kteam for kteam in range(10)]


ax = noiDungToanBoFile.splitlines()
temp=""
for i in ax:
    temp=temp+i
print(type(temp))
#xx=""+12+"" 
giaTriCapNhat[1]=noiDungToanBoFile 
truongCapNhat[1]='DataJson'

a.boSung1BanGhiDuLieuVaoCSDL(conn,"home_serverdataenglish",giaTriCapNhat,truongCapNhat,1)

# Bổ sung giá trị 1 Trường
'''giaTriCapNhat = [kteam for kteam in range(10)]
truongCapNhat = [kteam for kteam in range(10)]

giaTriCapNhat[1]='topic1'
truongCapNhat[1]='tentopichocvienchon'

a.boSung1BanGhiDuLieuVaoCSDL(conn,"english",giaTriCapNhat,truongCapNhat,1)'''

# 2)Form cập nhật 1 bản ghi tại 1 cột trong 1 bảng SQL

'''tenBang = 'appenglish_temptopic'
tenCot = 'TOPIC'
giaTriCapNhat = NULL
a.capNhat1GiaTriVao1CotCuaCSDL(conn, tenBang, tenCot, giaTriCapNhat)'''

# 3)Form cập nhật 1 bản ghi tại 1 cột trong 1 bảng SQL với id

'''tenBang = 'appenglish_temptopic'
tenCot = 'TOPICTEMP'
ID = 10
giaTriCapNhat = "None"
a.capNhat1GiaTriVao1CotCuaCSDLVoiDieuKienID(conn, tenBang, tenCot, giaTriCapNhat,ID)'''

# 3)FORM lấy 1 bản ghi tại 1 cột trong 1 bảng SQL
'''tenBang = 'english'
tenCot = 'tentopichocvienchon'
x = a.layGiaTriDauTienTai1CotCuaCSDL(conn,tenBang, tenCot)
print(x)'''

'''n = a.laySoLuongBanGhiCuaBang(conn,"appenglish_temptopic")
print(n)

tenBang = 'appenglish_temptopic'
tenCot = 'TOPICTEMP'
a.taoBangNull(conn,tenBang,tenCot)'''

'''truongCapNhat = [kteam for kteam in range(10)]

tenBang = 'appenglish_temptopic'
truongCapNhat[1]='TOPICTEMP'
#a.boSung1BanGhiNULLVaoCSDL(conn,tenBang,truongCapNhat,1)

soDongDuLieuMongoDB=5
soLuongBanGhiCuaBang=a.laySoLuongBanGhiCuaBang(conn,"appenglish_temptopic",truongCapNhat[1])

#a.taoBangNull(conn,tenBang,truongCapNhat[1])
if soDongDuLieuMongoDB > soLuongBanGhiCuaBang:
    a.resetIndex(conn,tenBang)
    for i in range (0,soDongDuLieuMongoDB-soLuongBanGhiCuaBang):
        a.boSung1BanGhiNULLVaoCSDL(conn,tenBang,truongCapNhat,1)
elif soDongDuLieuMongoDB<soLuongBanGhiCuaBang:
        a.xoaDongNull(conn,tenBang,truongCapNhat[1])'''

