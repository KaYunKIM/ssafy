from django.shortcuts import render

# Create your views here.
def card(request):
    articles = [
        ['test title1', 'test content1'],
        ['test title2', 'test content2'],
        ['test title3', 'test content3'],
        ['test title4', 'test content4'],
        ['test title5', 'test content5'],

    ]
    context = {
        'articles': articles,
    }
    return render(request, 'card.html', context)

def community(request):
    articles = [
        ['#', 'Title', 'Content', 'Creation Time'],
        ['test title 1', 'test content 1', 'test creation time1'],
        ['test title 2', 'test content 2', 'test creation time2'],
        ['test title 3', 'test content 3', 'test creation time3'],
        ['test title 4', 'test content 4', 'test creation time4'],
        ['test title 5', 'test content 5', 'test creation time5'],
        ['test title 6', 'test content 6', 'test creation time6'],
    ]

    context = {
        'articles': articles,

    }

    return render(request, 'community.html', context)