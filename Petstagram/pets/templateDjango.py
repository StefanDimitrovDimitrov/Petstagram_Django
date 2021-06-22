



def persist_pet(request,pet,template_name):

    if request.method == "GET":
        form = PetForm(instance=pet)

        context = {
            'form': form,
            'pet': pet,
        }

        return render(request, f'{template_name}.html', context)
    else:
        form = PetForm(
            request.POST,
            instance=pet
        )
        if form.is_valid():
            form.save()
            return redirect('pet details or comment', pet.pk)

        context = {
            'form': form,
            'pet': pet,
        }
        return render(request, f'{template_name}.html', context)




def edit_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    return persist_pet(request, pet, 'pet_edit')


def create_pet(request):
    pet = Pet()
    return persist_pet(request, pet, 'pet_create')


def delete_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'pet': pet,
        }
        return render(request, 'pet_delete.html', context)
    else:
        pet.delete()
        return redirect('list pets')



def persist_pet(request,OBJECT,template_name):
    form = OBJECTForm(instance=OBJECT)
    if request.method == "POST":
        form = OBJECTForm(request.POST,instance=OBJECT)

        if form.is_valid():
            form.save()
            return redirect('pet details or comment', OBJECT.pk)

    context = {
        'form': form,
        'OBJECT': OBJECT,
    }
    return render(request, f'{template_name}.html', context)


def edit_pet(request, pk):
    OBJECT = OBJECT.objects.get(pk=pk)
    return persist_pet(request, OBJECT, 'OBJECT_edit')


def create_pet(request):
    OBJECT = OBJECT()
    return persist_pet(request, OBJECT, 'OBJECT_create')


def delete_pet(request, pk):
    OBJECT = OBJECT.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'OBJECT': OBJECT,
        }
        return render(request, 'OBJECT_delete.html', context)
    else:
        OBJECT.delete()
        return redirect('list OBJECT')