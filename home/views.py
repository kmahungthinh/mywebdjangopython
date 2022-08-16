
from django.shortcuts import render, redirect
from .englishservice import *
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.http import Http404
from home.models import UserDataEnglish
import ast
with open('Data.txt', 'r', encoding='utf-8') as fileInp:
   jSonAll = fileInp.read()
jSonAll =ast.literal_eval(jSonAll)
dicDataPerson={}
def pageIndex(request):
   return render(request, 'pages/index.html')
from .forms import RegistrationForm
from django.http import HttpResponseRedirect
from django.contrib import messages
def pageDangKy(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Bạn đã đăng ký thành công!')
            return HttpResponseRedirect('/')
    return render(request, 'pages/dangky.html', {'form': form})
def pageChonChuyenDe(request):

   if str(request.user) == "AnonymousUser":
      messages.info(request, 'Bạn cần đăng nhập')
      return redirect('Index')
   else:
      if UserDataEnglish.objects.filter(nguoiDung=request.user).exists()==False:
         upd = UserDataEnglish(nguoiDung=request.user,TopicChoose='1',ExerciseChoose='2')
         upd.save()

      print("Chuyên đề comback")
      el = ChuyenDe(jSonAll)
      Data = {'LISTTOPIC': el}
      if request.method == 'POST':
         sttChuyenDeHocVienChon = request.POST.getlist('namechuyende')
         upd = UserDataEnglish.objects.get(id=UserDataEnglish.objects.get(nguoiDung=request.user).pk)
         upd.TopicChoose = "@topic" + str(int(sttChuyenDeHocVienChon[0]))
         upd.save()
         return redirect('ChonExercise')
   return render(request, 'pages/chonchuyende.html', Data)
def pageChonExercise(request):
   if str(request.user) == "AnonymousUser":
      messages.info(request, 'Bạn cần đăng nhập')
      return redirect('Index')
   else:
      #print("xx",UserDataEnglish.objects.get(id=User.objects.get(nguoiDung=request.user)))
      gt=UserDataEnglish.objects.get(id=UserDataEnglish.objects.get(nguoiDung=request.user).pk)
      el = Exercise(jSonAll, gt.TopicChoose)
      Data = {'LISTEXERCISE': el}
      if request.method == 'POST':

         sttExerciseHocVienChon = request.POST.getlist('nameexercise')

         upd = UserDataEnglish.objects.get(id=UserDataEnglish.objects.get(nguoiDung=request.user).pk)
         upd.ExerciseChoose = "@exercise" + str(int(sttExerciseHocVienChon[0]))
         upd.save()
         get = UserDataEnglish.objects.get(id=UserDataEnglish.objects.get(nguoiDung=request.user).pk)
         CHECK = jSonAll[get.TopicChoose][get.ExerciseChoose]["@check"]
         print(CHECK)
         if CHECK == "QUESTION_ABCD":
            return redirect('QUESTION_ABCD')
         if CHECK == "ABCD":
            return redirect('ABCD')
         if CHECK == "BIENDOICAU":
            return redirect('BIENDOICAU')
         if CHECK == "TEXT":
            return redirect('TEXT')
         if CHECK == "TIMVASUALOISAI":
            return redirect('TIMVASUALOISAI')
   return render(request, 'pages/chonexercise.html',Data)
def pageChonQuestion_ABCD(request):
   if str(request.user) == "AnonymousUser":
      messages.info(request, 'Bạn cần đăng nhập')
      return redirect('Index')
   else:
      gt = UserDataEnglish.objects.get(id=UserDataEnglish.objects.get(nguoiDung=request.user).pk)
      dataLamBaiTap1 = layDataPart1LamBaiTapQuestionABCD(jSonAll, gt.TopicChoose
                                                         , gt.ExerciseChoose)
      book_paginator = Paginator(dataLamBaiTap1, 1)
      page_num = request.GET.get('page')
      page = book_paginator.get_page(page_num)

      dataLamBaiTap2 = [gt.TopicChoose.lstrip("@")
         , gt.ExerciseChoose.lstrip("@")
         , jSonAll[gt.TopicChoose][gt.ExerciseChoose]["@title"], str(book_paginator.count)]

      context = {
         'page': page,
         'data2': dataLamBaiTap2
      }
      if request.method == 'POST' and 'kiemtra' in request.POST:
         gt = UserDataEnglish.objects.get(id=UserDataEnglish.objects.get(nguoiDung=request.user).pk)
         dapAnChon = request.POST.getlist('ABCD')
         if len(dapAnChon) == 0:
            messages.info(request, 'Xin lỗi! Bạn cần chọn 1 đáp án')
         else:
            dapAnChon = dapAnChon[0]
            print("Chọn tại page num: ", page.number)
            dapAnChinhXac = jSonAll[gt.TopicChoose][gt.ExerciseChoose]["@answer"][page.number - 1].lstrip("&")
            print("Chọn án bạn chọn: ", dapAnChon)
            print("Đáp án đúng ở câu này: ", dapAnChinhXac)
            if dapAnChon == dapAnChinhXac:
               messages.info(request, 'Rất tốt! Bạn đã làm chính xác')
            else:
               messages.info(request, 'Rất tiếc! Bạn đã làm sai')
      if request.method == 'POST' and 'goiy' in request.POST:
         gt = UserDataEnglish.objects.get(id=UserDataEnglish.objects.get(nguoiDung=request.user).pk)
         goiYDapAn = jSonAll[gt.TopicChoose][gt.ExerciseChoose]["@suggest"][page.number - 1].lstrip("^")
         messages.info(request, goiYDapAn)
      if request.method == 'POST' and 'quaylai' in request.POST:

         return redirect('ChonExercise')
   return render(request,'pages/lambaitap/QUESTION_ABCD.html',context)

def pageChonABCD(request):
   gt = UserDataEnglish.objects.get(id=UserDataEnglish.objects.get(nguoiDung=request.user).pk)
   if str(request.user) == "AnonymousUser":
      messages.info(request, 'Bạn cần đăng nhập')
      return redirect('Index')
   else:

      dataLamBaiTap1 = layDataPart1LamBaiTapABCD(jSonAll, gt.TopicChoose, gt.ExerciseChoose)
      book_paginator = Paginator(dataLamBaiTap1, 1)
      page_num = request.GET.get('page')
      page = book_paginator.get_page(page_num)

      dataLamBaiTap2 = [gt.TopicChoose.lstrip("@"), gt.ExerciseChoose.lstrip("@")
         , jSonAll[gt.TopicChoose][gt.ExerciseChoose]["@title"], str(book_paginator.count)]

      context = {
         'page': page,
         'data1': dataLamBaiTap1,
         'data2': dataLamBaiTap2
      }
      if request.method == 'POST' and 'kiemtra' in request.POST:
         gt = UserDataEnglish.objects.get(id=UserDataEnglish.objects.get(nguoiDung=request.user).pk)
         dapAnChon = request.POST.getlist('ABCD')
         if len(dapAnChon) == 0:
            messages.info(request, 'Xin lỗi! Bạn cần chọn 1 đáp án')
         else:
            dapAnChon = dapAnChon[0]
            print("dapAnChon", dapAnChon)
            print("Chọn tại page num: ", page.number)
            dapAnChinhXac = jSonAll[gt.TopicChoose][gt.ExerciseChoose]["@answer"][page.number - 1].lstrip("&")
            print("Chọn án bạn chọn: ", dapAnChon)
            print("Đáp án đúng ở câu này: ", dapAnChinhXac)
            if dapAnChon == dapAnChinhXac:
               messages.info(request, 'Rất tốt! Bạn đã làm chính xác')
            else:
               messages.info(request, 'Rất tiếc! Bạn đã làm sai')
      if request.method == 'POST' and 'goiy' in request.POST:
         gt = UserDataEnglish.objects.get(id=UserDataEnglish.objects.get(nguoiDung=request.user).pk)
         goiYDapAn = jSonAll[gt.TopicChoose][gt.ExerciseChoose]["@suggest"][page.number - 1].lstrip("^")
         messages.info(request, goiYDapAn)
      if request.method == 'POST' and 'quaylai' in request.POST:

         return redirect('ChonExercise')
   return render(request, 'pages/lambaitap/ABCD.html', context)


def pageChonTEXT(request):
   if str(request.user) == "AnonymousUser":
      messages.info(request, 'Bạn cần đăng nhập')
      return redirect('Index')
   else:
      gt = UserDataEnglish.objects.get(id=UserDataEnglish.objects.get(nguoiDung=request.user).pk)
      dataLamBaiTap1 = layDataPart1LamBaiTapTEXT(jSonAll, gt.TopicChoose, gt.ExerciseChoose)
      book_paginator = Paginator(dataLamBaiTap1, 1)
      page_num = request.GET.get('page')
      page = book_paginator.get_page(page_num)

      dataLamBaiTap2 = [gt.TopicChoose.lstrip("@"), gt.ExerciseChoose.lstrip("@")
         , jSonAll[gt.TopicChoose][gt.ExerciseChoose]["@title"], str(book_paginator.count)]

      context = {
         'page': page,
         'data2': dataLamBaiTap2,
      }
      if request.method == 'POST' and 'kiemtra' in request.POST:
         gt = UserDataEnglish.objects.get(id=UserDataEnglish.objects.get(nguoiDung=request.user).pk)
         dapAnChon = ""
         for i in dataLamBaiTap1[page.number - 1][2]:
            dapAnChon += "*|" + request.POST.getlist(i)[0]
         if len(dapAnChon) > 100:
            messages.info(request, "Xin lỗi! Trường nhập bất thường")
         else:
            DataDapAnKhaDung = layDataDapAnKhaDung(
               jSonAll[gt.TopicChoose][gt.ExerciseChoose]["@answer"][page.number - 1])

            print("Chọn án bạn chọn: ", dapAnChon)
            check = dapAnChon.replace("’", "'") in DataDapAnKhaDung
            if check == True:
               messages.info(request, 'Rất tốt! Bạn đã làm chính xác')
            else:
               messages.info(request, 'Rất tiếc! Bạn đã làm sai')
      if request.method == 'POST' and 'goiy' in request.POST:
         gt = UserDataEnglish.objects.get(id=UserDataEnglish.objects.get(nguoiDung=request.user).pk)
         goiYDapAn = jSonAll[gt.TopicChoose][gt.ExerciseChoose]["@suggest"][page.number - 1].lstrip("^")
         messages.info(request, goiYDapAn)
      if request.method == 'POST' and 'quaylai' in request.POST:

         return redirect('ChonExercise')
   return render(request, 'pages/lambaitap/TEXT.html', context)


def pageChonBIENDOICAU(request):
   if str(request.user) == "AnonymousUser":
      messages.info(request, 'Bạn cần đăng nhập')
      return redirect('Index')
   else:
      gt = UserDataEnglish.objects.get(id=UserDataEnglish.objects.get(nguoiDung=request.user).pk)
      dataLamBaiTap1 = layDataPart1LamBaiTapBienDoiCau(jSonAll, gt.TopicChoose, gt.ExerciseChoose)
      book_paginator = Paginator(dataLamBaiTap1, 1)
      page_num = request.GET.get('page')
      page = book_paginator.get_page(page_num)

      dataLamBaiTap2 = [gt.TopicChoose.lstrip("@"), gt.ExerciseChoose.lstrip("@")
         , jSonAll[gt.TopicChoose][gt.ExerciseChoose]["@title"], str(book_paginator.count)]

      context = {
         'page': page,
         'data2': dataLamBaiTap2,
      }
      if request.method == 'POST' and 'kiemtra' in request.POST:
         gt = UserDataEnglish.objects.get(id=UserDataEnglish.objects.get(nguoiDung=request.user).pk)
         print("Chọn tại page num: ", page.number)
         dapAnChon = ""
         for i in dataLamBaiTap1[page.number - 1][3]:
            dapAnChon += "*|" + request.POST.getlist(i)[0]
         if len(dapAnChon) > 100:
            messages.info(request, "Xin lỗi! Trường nhập bất thường")
         else:
            DataDapAnKhaDung = layDataDapAnKhaDung(
               jSonAll[gt.TopicChoose][gt.ExerciseChoose]["@answer"][page.number - 1])

            print("Chọn án bạn chọn: ", dapAnChon)
            check1 = dapAnChon.replace("’", "'") in DataDapAnKhaDung
            check2 = dapAnChon.replace("’", "'").replace(".", "") in DataDapAnKhaDung
            if check1 == True or check2 == True:
               messages.info(request, 'Rất tốt! Bạn đã làm chính xác')
            else:
               messages.info(request, 'Rất tiếc! Bạn đã làm sai')
      if request.method == 'POST' and 'goiy' in request.POST:
         gt = UserDataEnglish.objects.get(id=UserDataEnglish.objects.get(nguoiDung=request.user).pk)
         goiYDapAn = jSonAll[gt.TopicChoose][gt.ExerciseChoose]["@suggest"][page.number - 1].lstrip("^")
         messages.info(request, goiYDapAn)
      if request.method == 'POST' and 'quaylai' in request.POST:
         return redirect('ChonExercise')
   return render(request,'pages/lambaitap/BIENDOICAU.html',context)
def pageTimVaSuaLoiSai(request):
   if str(request.user) == "AnonymousUser":
      messages.info(request, 'Bạn cần đăng nhập')
      return redirect('Index')
   else:
      gt = UserDataEnglish.objects.get(id=UserDataEnglish.objects.get(nguoiDung=request.user).pk)
      dataLamBaiTap1 = layDataPart1LamBaiTapTEXT(jSonAll, gt.TopicChoose, gt.ExerciseChoose)
      book_paginator = Paginator(dataLamBaiTap1, 1)
      page_num = request.GET.get('page')
      page = book_paginator.get_page(page_num)

      dataLamBaiTap2 = [gt.TopicChoose.lstrip("@"), gt.ExerciseChoose.lstrip("@")
         , jSonAll[gt.TopicChoose][gt.ExerciseChoose]["@title"], str(book_paginator.count)]

      context = {
         'page': page,
         'data2': dataLamBaiTap2,
      }
      if request.method == 'POST' and 'kiemtra' in request.POST:
         print("Chọn tại page num: ", page.number)
         dapAnChon = ""
         for i in dataLamBaiTap1[page.number - 1][2]:
            dapAnChon += "*|" + request.POST.getlist(i)[0]
         if len(dapAnChon) > 100:
            messages.info(request, "Xin lỗi! Trường nhập bất thường")
         else:
            DataDapAnKhaDung = layDataDapAnKhaDung(
               jSonAll[gt.TopicChoose][gt.ExerciseChoose]["@answer"][page.number - 1])

            print("Chọn án bạn chọn: ", dapAnChon)
            check = dapAnChon.replace("’", "'") in DataDapAnKhaDung
            if check == True:
               messages.info(request, 'Rất tốt! Bạn đã làm chính xác')
            else:
               messages.info(request, 'Rất tiếc! Bạn đã làm sai')

      if request.method == 'POST' and 'goiy' in request.POST:
            gt = UserDataEnglish.objects.get(id=UserDataEnglish.objects.get(nguoiDung=request.user).pk)
            goiYDapAn = jSonAll[gt.TopicChoose][gt.ExerciseChoose]["@suggest"][page.number - 1].lstrip("^")
            messages.info(request, goiYDapAn)
      if request.method == 'POST' and 'quaylai' in request.POST:

            return redirect('ChonExercise')
   return render(request, 'pages/lambaitap/TIMVASUALOISAI.html', context)


def error(request,*args,**kwargs):
   return render(request,'pages/error.html')