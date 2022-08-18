
from pymongo import MongoClient
import urllib.parse
import itertools

'''class JSonAll():
    username = urllib.parse.quote_plus("")
    password = urllib.parse.quote_plus("")
    # URL kết nối
    url = "mongodb+srv://{}:{}@cluster0.mntkkke.mongodb.net/?retryWrites=true&w=majority".format(username, password)
    cluster = MongoClient(url)
    # Tên collection
    db = cluster['ServerEnglish']
    # Tên document
    collection = db['App']
    # Lấy toàn bộ json
    jSonAll=None
    for doc in collection.find():
        jSonAll = doc'''

def xoaGiaTriNoneKhoiDic(_dict):
        """Delete None values recursively from all of the dictionaries, tuples, lists, sets"""
        if isinstance(_dict, dict):
            for key, value in list(_dict.items()):
                if isinstance(value, (list, dict, tuple, set)):
                    _dict[key] = xoaGiaTriNoneKhoiDic(value)
                elif value is None or key is None:
                    del _dict[key]

        elif isinstance(_dict, (list, set, tuple)):
            _dict = type(_dict)(xoaGiaTriNoneKhoiDic(item) for item in _dict if item is not None)
        return _dict
def ChuyenDe(jSonAll):
    #Số lượng chuyên đề
    number = int(int(str(jSonAll).count("@topic")))
    CHUYENDE_CHOICES = []
    #Lấy danh sách tên chuyên đề theo chỉ mục json
    for i in range(1, number+1):
        CHUYENDE_CHOICES.append([str(i), jSonAll["@titletopic"]["@" + str(i)]])

    print(CHUYENDE_CHOICES)
    #Trả về danh sách topic
    return CHUYENDE_CHOICES
def Exercise(jSonAll, TOPICCHON):
    # Lấy json theo topic được chọn
    jsonExercise = jSonAll[TOPICCHON]
    # Số lượng exercise
    number = int(int(str(jsonExercise).count("@exercise")))
    EXERCISE_CHOICES = []
    # Lấy danh sách tên exercise theo chỉ mục json
    for i in range(1, number+1):
        EXERCISE_CHOICES.append([str(i),"Exercise " + str(i)])

    # Trả về danh sách exercise theo topic được chọn
    return EXERCISE_CHOICES

def layDataPart1LamBaiTapQuestionABCD(json,TENINDEXJSONTOPIC,TENINDEXJSONEXERCISE):
    a = json[TENINDEXJSONTOPIC][TENINDEXJSONEXERCISE]["@question"]
    b=json[TENINDEXJSONTOPIC][TENINDEXJSONEXERCISE]["@answer"]
    c=json[TENINDEXJSONTOPIC][TENINDEXJSONEXERCISE]["@suggest"]
    d=[]
    for i in range(0,len(a)):
        tempa=a[i].split("%")
        d.append([tempa[0].lstrip("#"),tempa[1],b[i].lstrip("&"),c[i].lstrip("^")])
    return d
def layDataPart1LamBaiTapABCD(json,TENINDEXJSONTOPIC,TENINDEXJSONEXERCISE):
    a = json[TENINDEXJSONTOPIC][TENINDEXJSONEXERCISE]["@question"]
    b=json[TENINDEXJSONTOPIC][TENINDEXJSONEXERCISE]["@answer"]
    c=json[TENINDEXJSONTOPIC][TENINDEXJSONEXERCISE]["@suggest"]
    d=[]
    for i in range(0,len(a)):
        d.append([a[i].lstrip("#"),b[i].lstrip("&"),c[i].lstrip("^")])
    return d
def layDataPart1LamBaiTapTEXT(json,TENINDEXJSONTOPIC,TENINDEXJSONEXERCISE):
    a = json[TENINDEXJSONTOPIC][TENINDEXJSONEXERCISE]["@question"]
    b=json[TENINDEXJSONTOPIC][TENINDEXJSONEXERCISE]["@suggest"]
    d=[]

    for i in range(0,len(a)):
        c = json[TENINDEXJSONTOPIC][TENINDEXJSONEXERCISE]["@answer"][i].count("*|")
        tempc = []
        for j in range(0,c):
            tempc.append(str(j+1))
        d.append([a[i].lstrip("#"),b[i].lstrip("^"),tempc])
    print(d)
    return d
def layDataPart1LamBaiTapBienDoiCau(json,TENINDEXJSONTOPIC,TENINDEXJSONEXERCISE):

    a = json[TENINDEXJSONTOPIC][TENINDEXJSONEXERCISE]["@question"]
    b = json[TENINDEXJSONTOPIC][TENINDEXJSONEXERCISE]["@answer"]
    d = json[TENINDEXJSONTOPIC][TENINDEXJSONEXERCISE]["@suggest"]
    e = []
    for i in range(0, len(a)):
        tempa = a[i].split("%")
        c = json[TENINDEXJSONTOPIC][TENINDEXJSONEXERCISE]["@answer"][i].count("*|")
        tempc = []
        for j in range(0, c):
            tempc.append(str(j + 1))
        e.append([tempa[0].lstrip("#"), tempa[1], b[i].lstrip("&"), tempc, d[i].lstrip("^")])
    return e
def layDataDapAnKhaDung(answerFireBase):
    # 1 Đưa đáp án đầu vào
    #answerFireBase = "*|were building"
    #answerFireBase = "*|were building|haven't finished| *|was|abc|def*|have not finished| | "
    print("Đáp án đầu vào")
    #print(answerFireBase)

    # 2) Tiền xử lý đáp án đầu vào về dạng list
    list1 = answerFireBase.split("*");
    # 3) Lấy số trường nhập đáp án
    soTruongNhapDapAn = answerFireBase.count("*|")
    print("Số trường nhập đáp án", soTruongNhapDapAn)

    # 4 Ma trận chuỗi nxk chuỗi đáp án  và lấy số đáp án trong 1 trường
    list2 = []
    soDapDapAnTrong1Truong = 0
    for i in range(1, soTruongNhapDapAn + 1):
        list2.append(list1[i].split("|"))
        list2[i - 1].remove('')
    soDapDapAnTrong1Truong = len(list2[0])
    for i in list2:
        if len(i) > soDapDapAnTrong1Truong:
            soDapDapAnTrong1Truong = len(list2[i])

    listTangDanDapAnTrong1Truong = []
    for i in range(1, soDapDapAnTrong1Truong + 1):
        listTangDanDapAnTrong1Truong.append(i)

    # 3) Lấy Danh sách chỉnh hợp lặp của 1,2 xếp mỗi bản ghi 3 vị trí số kết quả là 2^3
    chinhHopLapChapKCuaN = list(itertools.product(listTangDanDapAnTrong1Truong, repeat=soTruongNhapDapAn))

    print("Danh sách chỉnh hợp lặp")
    print(chinhHopLapChapKCuaN)

    # 4) Kết hợp tham số 1 và 2 đưa ra danh sách chỉnh hợp lặp
    dapAnDungKhaDung = []
    for i in list(chinhHopLapChapKCuaN):
        viTriCuaSoLuongDapAn = 0
        temp = ""
        for j in i:
            viTriCuaSoDapAnKhaThi = j - 1
            # print("vị trí số đáp án khả thi: ",viTriCuaSoDapAnKhaThi,"vị trí số lượng đáp án: ",viTriCuaSoLuongDapAn)
            # print(list2[viTriCuaSoLuongDapAn][viTriCuaSoDapAnKhaThi])
            temp = temp + "*|" + list2[viTriCuaSoLuongDapAn][viTriCuaSoDapAnKhaThi]
            viTriCuaSoLuongDapAn = viTriCuaSoLuongDapAn + 1
        # print("\n")
        check = "| " in temp
        if check == False:
            dapAnDungKhaDung.append(temp)
    print("Số Đáp án khả dụng", len(dapAnDungKhaDung))
    for i in dapAnDungKhaDung:
        print(i)
    return dapAnDungKhaDung









