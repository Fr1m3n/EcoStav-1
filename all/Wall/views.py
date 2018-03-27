from django.shortcuts import render

# Create your views here.


def WallRender(request):
    q = 'QQQ'
    return render(request, 'wall/wall.html', locals())
