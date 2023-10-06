from django.db.models import Q
from .forms import MemberForm
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.template import loader
from members.forms import SimpleForm
from members.models import Member

# Create your views here.
def members(request):
    template = loader.get_template('all_members.html')
    member = Member.objects.all().order_by('firstName').values()
    context ={
        'member': member,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    template = loader.get_template('details.html')
    member = Member.objects.get(id = id)
    context = {
        'member': member,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def testing(request):
    template = loader.get_template('template.html')
    context = {
        'Fruits': ['apple', 'banana', 'pineapple']
    }
    return HttpResponse(template.render(context, request))

def show_form(request):
    form = SimpleForm()
    return render(request,'form.html', {'form':form})

def add_member(request):
    if request.method == 'POST':
        form = SimpleForm(request.POST)
        if form.is_valid():
            # Extract data from the form
            first_name = form.cleaned_data['firstName']
            last_name = form.cleaned_data['lastName']
            phone = form.cleaned_data.get('phone', '')  # Provide a default value (empty string) for phone
            date = form.cleaned_data.get('date', None)  # Provide None as default for date

            # Create a new Member instance and save it to the database
            member = Member(
                firstName=first_name,
                lastName=last_name,
                phone=phone,
                join_date=date,
            )
            member.save()

            # Redirect to a success page or members list
            
            return redirect('members')  # Redirect to the 'members' page or wherever you want

    else:
        form = SimpleForm()

    return render(request, 'form.html', {'form': form})

def edit_member(request, id):
    member = get_object_or_404(Member, pk=id)

    if request.method == 'POST':
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('details', id=id)
    else:
        form = MemberForm(instance=member)

    return render(request, 'edit_member.html', {'form': form, 'member': member})

def delete_member(request, id):
    member = get_object_or_404(Member, pk=id)
    
    if request.method == 'POST':
        member.delete()
        return redirect('members')  
    member.delete()
    return redirect('members')

def search_method(request):
    first_name = request.GET.get('first_name_search', '')
    last_name = request.GET.get('last_name_search', '')
    phone = request.GET.get('Phone_search', '')
    date = request.GET.get('Date_search', '')

    query = Q()

    if first_name:
        query |= Q(first_name__icontains = first_name)
    if last_name:
        query |= Q(last_name__icontains = last_name)
    if phone:
        query |= Q(Phone__icontains = phone)
    if date:
        query |= Q(join_date__icontains=date)

    search_result = Member.objects.filter('query')

    return render(request, 'search.html', {'search_result':search_result})

def search_form(request):
    return render(request, 'search.html')

def display_result(request):
    first_name = request.GET.get('first_name_search', '')
    last_name = request.GET.get('last_name_search', '')
    phone = request.GET.get('Phone_search', '')
    date = request.GET.get('Date_search', '')

    search_result = Member.objects.filter(
        firstName__icontains=first_name,
        lastName__icontains=last_name,
        phone__icontains=phone,
        join_date__icontains=date
    )

    return render(request, 'search_results.html', {'search_result': search_result})


# def delete_confirmation(request, id):
#     member = get_object_or_404(Member, pk=id)
#     member.delete()
    
#     return render(request, 'delete_confirmation.html', {'member': member})
