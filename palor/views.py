from django.shortcuts import render,redirect
from .models import category,Photo

# Create your views here.
def gallery(request):
    categories = category.objects.all()
    photos = Photo.objects.all()
    context = {'categories': categories, 'photos': photos}
    return render(request,'photos/gallery.html', context)


def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request,'photos/photo.html', {'photo': photo})


def addPhoto(request):
    categories = category.objects.all()

    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')

        if data['category'] != 'none':
            category = category.objects.get(id=data['category'])

        elif data['category_new'] != '':
            category, created = category.objects.get_or_create(name=data['category_new'])

        else:
            category = None

        photo = Photo.objects.create(
            category = category,
            description=data['description'],
            image = image,
        )
        return redirect('palor')

    context = {'categories': categories}
    return render(request,'photos/add.html', context)