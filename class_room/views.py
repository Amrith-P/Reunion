from django.shortcuts import render, redirect
from class_room.models import *
from django.db import IntegrityError
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


def list_benches(request):
    bench11 = Bench11.objects.all()
    bench12 = Bench12.objects.all()
    bench13 = Bench13.objects.all()
    bench14 = Bench14.objects.all()
    bench15 = Bench15.objects.all()
    bench21 = Bench21.objects.all()
    bench22 = Bench22.objects.all()
    bench23 = Bench23.objects.all()
    bench24 = Bench24.objects.all()
    bench25 = Bench25.objects.all()
    bench26 = Bench26.objects.all()
    


    context = {
        'bench11': bench11,
        'bench12': bench12,
        'bench13': bench13,
        'bench14': bench14,
        'bench15': bench15,
        'bench21': bench21,
        'bench22': bench22,
        'bench23': bench23,
        'bench24': bench24,
        'bench25': bench25,
        'bench26': bench26,



    }
    return render(request, 'index.html', context)


def edit_bench11(request, bench_id):
    bench11 = Bench11.objects.get(id=bench_id)

    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        student_image = request.FILES.get('student_image')
        bench11.student_name = student_name
        bench11.student_image = student_image
        try:
            bench11.save()
            messages.success(request, f" '{bench11.student_name}' Details Added Successfully")
            return redirect('/')
        except IntegrityError:
            messages.error(request, f" '{bench11.student_name}' Field")
            return redirect('edit_bench11', bench_id=bench_id)
    context = {
        'bench11': bench11,
    }
    return render(request, 'edit_bench11.html', context)

def edit_bench12(request, bench_id):
    bench12 = Bench12.objects.get(id=bench_id)

    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        student_image = request.FILES.get('student_image')
        bench12.student_name = student_name
        bench12.student_image = student_image
        try:
            bench12.save()
            messages.success(request, f" '{bench12.student_name}' Details Added Successfully")
            return redirect('/')
        except IntegrityError:
            messages.error(request, f" '{bench12.student_name}' Field")
            return redirect('edit_bench12', bench_id=bench_id)
    context = {
        'bench12': bench12,
    }
    return render(request, 'edit_bench12.html', context)    

def edit_bench13(request, bench_id):
    bench13 = Bench13.objects.get(id=bench_id)

    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        student_image = request.FILES.get('student_image')
        bench13.student_name = student_name
        bench13.student_image = student_image
        try:
            bench13.save()
            messages.success(request, f" '{bench13.student_name}' Details Added Successfully")
            return redirect('/')
        except IntegrityError:
            messages.error(request, f" '{bench13.student_name}' Field")
            return redirect('edit_bench13', bench_id=bench_id)
    context = {
        'bench13': bench13,
    }
    return render(request, 'edit_bench13.html', context)

def edit_bench14(request, bench_id):
    bench14 = Bench14.objects.get(id=bench_id)

    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        student_image = request.FILES.get('student_image')
        bench14.student_name = student_name
        bench14.student_image = student_image
        try:
            bench14.save()
            messages.success(request, f" '{bench14.student_name}' Details Added Successfully")
            return redirect('/')
        except IntegrityError:
            messages.error(request, f" '{bench14.student_name}' Field")
            return redirect('edit_bench14', bench_id=bench_id)
    context = {
        'bench14': bench14,
    }
    return render(request, 'edit_bench14.html', context)

def edit_bench15(request, bench_id):
    bench15 = Bench15.objects.get(id=bench_id)

    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        student_image = request.FILES.get('student_image')
        bench15.student_name = student_name
        bench15.student_image = student_image
        try:
            bench15.save()
            messages.success(request, f" '{bench15.student_name}' Details Added Successfully")
            return redirect('/')
        except IntegrityError:
            messages.error(request, f" '{bench15.student_name}' Field")
            return redirect('edit_bench15', bench_id=bench_id)
    context = {
        'bench15': bench15,
    }
    return render(request, 'edit_bench15.html', context) 

def edit_bench21(request, bench_id):
    bench21 = Bench21.objects.get(id=bench_id)

    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        student_image = request.FILES.get('student_image')
        bench21.student_name = student_name
        bench21.student_image = student_image
        try:
            bench21.save()
            messages.success(request, f" '{bench21.student_name}' Details Added Successfully")
            return redirect('/')
        except IntegrityError:
            messages.error(request, f" '{bench21.student_name}' Field")
            return redirect('edit_bench21', bench_id=bench_id)
    context = {
        'bench12': bench21,
    }
    return render(request, 'edit_bench21.html', context)  

def edit_bench22(request, bench_id):
    bench22 = Bench12.objects.get(id=bench_id)

    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        student_image = request.FILES.get('student_image')
        bench22.student_name = student_name
        bench22.student_image = student_image
        try:
            bench22.save()
            messages.success(request, f" '{bench22.student_name}' Details Added Successfully")
            return redirect('/')
        except IntegrityError:
            messages.error(request, f" '{bench22.student_name}' Field")
            return redirect('edit_bench22', bench_id=bench_id)
    context = {
        'bench22': bench22,
    }
    return render(request, 'edit_bench22.html', context)      

def edit_bench23(request, bench_id):
    bench23 = Bench23.objects.get(id=bench_id)

    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        student_image = request.FILES.get('student_image')
        bench23.student_name = student_name
        bench23.student_image = student_image
        try:
            bench23.save()
            messages.success(request, f" '{bench23.student_name}' Details Added Successfully")
            return redirect('/')
        except IntegrityError:
            messages.error(request, f" '{bench23.student_name}' Field")
            return redirect('edit_bench12', bench_id=bench_id)
    context = {
        'bench23': bench23,
    }
    return render(request, 'edit_bench23.html', context) 

def edit_bench24(request, bench_id):
    bench24 = Bench24.objects.get(id=bench_id)

    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        student_image = request.FILES.get('student_image')
        bench24.student_name = student_name
        bench24.student_image = student_image
        try:
            bench24.save()
            messages.success(request, f" '{bench24.student_name}' Details Added Successfully")
            return redirect('/')
        except IntegrityError:
            messages.error(request, f" '{bench24.student_name}' Field")
            return redirect('edit_bench24', bench_id=bench_id)
    context = {
        'bench24': bench24,
    }
    return render(request, 'edit_bench24.html', context)      

def edit_bench25(request, bench_id):
    bench25 = Bench25.objects.get(id=bench_id)

    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        student_image = request.FILES.get('student_image')
        bench25.student_name = student_name
        bench25.student_image = student_image
        try:
            bench25.save()
            messages.success(request, f" '{bench25.student_name}' Details Added Successfully")
            return redirect('/')
        except IntegrityError:
            messages.error(request, f" '{bench25.student_name}' Field")
            return redirect('edit_bench25', bench_id=bench_id)
    context = {
        'bench25': bench25,
    }
    return render(request, 'edit_bench25.html', context)  

def edit_bench26(request, bench_id):
    bench26 = Bench26.objects.get(id=bench_id)

    if request.method == 'POST':
        student_name = request.POST.get('student_name')
        student_image = request.FILES.get('student_image')
        bench26.student_name = student_name
        bench26.student_image = student_image
        try:
            bench26.save()
            messages.success(request, f" '{bench26.student_name}' Details Added Successfully")
            return redirect('/')
        except IntegrityError:
            messages.error(request, f" '{bench26.student_name}' Field")
            return redirect('edit_bench26', bench_id=bench_id)
    context = {
        'bench26': bench26,
    }
    return render(request, 'edit_bench26.html', context)        