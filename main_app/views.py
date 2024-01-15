from django.shortcuts import render

groups = [
  {'name': 'GirlsTrip 2024', 'description': 'Girls trip to Napa in 2024','members':'You, User 2, User 3, User 4',},
  {'name': 'House Expenses', 'description': 'Monthly house expenses','members':'You, User 2, User 4',},
]

def home(request):
    return render(request, 'home.html')

def groups_index(request):
    return render(request, 'groups/groups_index.html', {
        'groups': groups
    })

def expenses(request):
    return render(request, 'expenses.html')