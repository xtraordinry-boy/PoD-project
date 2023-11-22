from django.shortcuts import render
from django.http import JsonResponse
from .models import User, Store, Design, Order

def user_registration(request):
  if request.method == 'POST':
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']

    try:
      User.objects.create(username=username, email=email, password=password)
      return JsonResponse({'success': True, 'message': 'User registered successfully'})
    except IntegrityError:
      return JsonResponse({'success': False, 'message': 'Username or email already exists'})
  else:
    return render(request, 'registration.html')

def store_creation(request):
  if request.method == 'POST':
    owner_id = request.POST['owner_id']
    name = request.POST['name']
    description = request.POST['description']

    try:
      Store.objects.create(owner_id=owner_id, name=name, description=description)
      return JsonResponse({'success': True, 'message': 'Store created successfully'})
    except ValueError:
      return JsonResponse({'success': False, 'message': 'Invalid owner ID'})
  else:
    return render(request, 'store_creation.html')

def design_upload(request):
  if request.method == 'POST':
    if request.FILES:
      design_file = request.FILES['file']
      user_id = request.POST.get('user_id')
      store_id = request.POST.get('store_id')
      name = request.POST.get('name')
      description = request.POST.get('description')

      if user_id and store_id and name and description:
        with transaction.atomic():
          design = Design(
              user_id=user_id,
              store_id=store_id,
              name=name,
              description=description,
          )
          design.save()
          design_filename = f"{design.id}.{design_file.extension}"
          design.image.save(design_filename, design_file)
          design.save()

          return JsonResponse({'success': True, 'message': 'Design uploaded successfully'})
      else:
        return JsonResponse({'success': False, 'message': 'Missing required parameters'})
    else:
      return JsonResponse({'success': False, 'message': 'No file uploaded'})
  else:
    return HttpResponse('Invalid request method')

def retrieve_designs(request):
  if request.method == 'GET':
    user_id = request.GET.get('user_id')
    store_id = request.GET.get('store_id')

    if user_id:
      designs = Design.objects.filter(user_id=user_id)
    elif store_id:
      designs = Design.objects.filter(store_id=store_id)
    else:
      designs = Design.objects.all()

    design_data = []
    for design in designs:
      design_data.append({
          'id': design.id,
          'name': design.name,
          'description': design.description,
          'image_url': design.image.url,
      })

    return JsonResponse({'designs': design_data})

def delete_design(request):
  if request.method == 'DELETE':
    design_id = request.POST.get('design_id')

    if design_id:
      design = Design.objects.get(id=design_id)
      design.delete()

      return JsonResponse({'success': True, 'message': 'Design deleted successfully'})
    else:
      return JsonResponse({'success': False, 'message': 'Missing required parameters'})
  else:
    return HttpResponse('Invalid request method

