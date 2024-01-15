from django.shortcuts import render


# groups = [
#   {'name': 'Girls Trip 2024', 'description': 'Girls trip to Napa in 2024','members':'You, User 2, User 3, User 4',},
#   {'name': 'House Expenses', 'description': 'Monthly house expenses','members':'You, User 2, User 4',},
# ]

# expenses = [
#   {'group': 'Girls Trip 2024', 'title': 'Airfare', 'type': 'Travel', 'description': 'Round trip flights from Boston to Napa', 'amount': '$1,200', 'split': '4'},
#   {'group': 'House Expenses', 'title': 'Rent', 'type': 'Housing', 'description': 'Rent for January', 'amount': '$1,000', 'split': '3'},
# ]

def home(request):
    return render(request, 'home.html')

def groups_index(request):
    return render(request, 'groups/groups_index.html', {
        'groups': groups
    })

def expenses_index(request):
    return render(request, 'expenses/expenses_index.html', {
        'expenses': expenses
    })