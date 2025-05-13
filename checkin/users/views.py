from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import CheckIn
from datetime import datetime, timedelta
import calendar

@login_required
def checkin_index(request):
    today = timezone.now().date()
    checkins = CheckIn.objects.filter(user=request.user).order_by('-date', '-time')
    return render(request, 'checkinindex.html', {
        'checkins': checkins,
        'today': today
    })

@login_required
def new_checkin(request):
    if request.method == 'POST':
        location = request.POST.get('location')
        notes = request.POST.get('notes')
        
        # 檢查今天是否已經簽到
        today = timezone.now().date()
        if CheckIn.objects.filter(user=request.user, date=today).exists():
            messages.error(request, '今天已經簽到過了！')
            return redirect('checkin_index')
        
        CheckIn.objects.create(
            user=request.user,
            location=location,
            notes=notes
        )
        messages.success(request, '簽到成功！')
        return redirect('checkin_index')
    
    return render(request, 'new_checkin.html')

@login_required
def edit_checkin(request, checkin_id):
    checkin = get_object_or_404(CheckIn, id=checkin_id, user=request.user)
    
    if request.method == 'POST':
        checkin.location = request.POST.get('location')
        checkin.notes = request.POST.get('notes')
        checkin.save()
        messages.success(request, '簽到記錄已更新！')
        return redirect('checkin_index')
    
    return render(request, 'edit_checkin.html', {'checkin': checkin})

@login_required
def delete_checkin(request, checkin_id):
    checkin = get_object_or_404(CheckIn, id=checkin_id, user=request.user)
    
    if request.method == 'POST':
        checkin.delete()
        messages.success(request, '簽到記錄已刪除！')
        return redirect('checkin_index')
    
    return render(request, 'delete_confirm.html', {'checkin': checkin})

@login_required
def calendar_view(request):
    today = timezone.now().date()
    year = request.GET.get('year', today.year)
    month = request.GET.get('month', today.month)
    
    try:
        year = int(year)
        month = int(month)
    except ValueError:
        year = today.year
        month = today.month
    
    cal = calendar.monthcalendar(year, month)
    checkins = CheckIn.objects.filter(
        user=request.user,
        date__year=year,
        date__month=month
    )
    
    # 創建一個字典來存儲每天的簽到狀態
    checkin_dates = {checkin.date.day: checkin for checkin in checkins}
    
    return render(request, 'calendar.html', {
        'calendar': cal,
        'year': year,
        'month': month,
        'checkin_dates': checkin_dates,
        'month_name': calendar.month_name[month]
    })

@login_required
def checkin_form(request):
    return render(request, 'checkin_form.html') 