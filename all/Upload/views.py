from django.shortcuts import render, redirect
from .forms import UploadForm
import os
from Ecopolice.settings import neuro_path, media_path
from Upload.models import Image
from PIL import Image as pil_img


def upload(request):
    # Форма загрузки изображения
    print(request.method)
    # test = request.method
    title = 'Upload Image'
    all_imgs = Image.objects.all()
    if request.method == 'POST':
        print(111)
        # подгружаем форму модели
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            # сохраняем поле
            new_form = form.save(commit=False)
            new_form.path_toResult = '/upload/result/' + str(request.FILES['image'])
            new_form.save()
            # перенаправление на страницу обработки
            return redirect(new_form.path_toResult)
    else:
        form = UploadForm()
    return render(request, 'uploadImage/upload.html', locals())


def result(request):
    global img
    title = 'Result'
    # имя изображения из URL  (пример: http://localhost:8000/upload/result/IMG_7071.JPG -> IMG_7071.JPG
    image_name = str(request.path).split('/')[3]
    # переменная для поиска поля в БД
    dbSearch_str = 'data/' + image_name
    # объект поля для HTML
    exist = False
    # проверка существования записи в БД для этого фото
    try:
        img = Image.objects.get(image=dbSearch_str)
        exist = True
    except:
        pass
    # полный путь до фото
    full_path = media_path + '/data/' + image_name
    Result = None
    if exist == True:
        if img.neuro_result == 'None':
            # вызов нейросети для обработки изображения
            os.system('python ' + neuro_path + '/classify_image.py --image_file ' + full_path)
            # открыть файл с выводом нейросети
            result_file = open(neuro_path + '/out.txt', 'r')
            # считать файл и разделить его по строкам (":" - конец строки) для HTML
            Result = result_file.read()
            # записать в БД ответ нейросети
            img.neuro_result = Result
            img.save()
            # закрыть файл
            result_file.close()
        else:
            Result = img.neuro_result
        # разделяй и влавствуй
        Result = Result.split(':')
    # открыть файл с помощью pillow, для масштабирования
    pimg = pil_img.open(full_path)
    # получить коефициент для масштабирования
    k = pimg.size[1] / 400
    print(k)
    # задать высоту и ширину изображения для HTML
    hgt = int(pimg.size[1] / k)
    wdt = int(pimg.size[0] / k)
    # приберём за собой с:
    del pimg
    return render(request, 'uploadImage/result.html', locals())
