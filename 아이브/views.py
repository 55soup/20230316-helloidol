from django.shortcuts import render

def show_원영(request):
    context={
        'name' : '장원영',
        'img_src': 'https://talkimg.imbc.com/TVianUpload/tvian/TViews/image/2023/02/02/ea1a4183-3441-4cdc-ae7f-e24be7506eb2.jpg',
    }
    return render(request, '아이브/원영.html', context=context)

def show_유진(request):
    context={
        'name' : '안유진',
        'img_src' : 'https://img.theqoo.net/img/UKCYA.png',
    }
    return render(request, '아이브/유진.html', context=context)
