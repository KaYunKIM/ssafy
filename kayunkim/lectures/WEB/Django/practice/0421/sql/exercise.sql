User.objects.all().values()


User.objects.filter(id=19).values('age')


User.objects.values('age')


User.objects.filter(age__lte=40).values('id','balance')


User.objects.filter(last_name='김', balance__gte=500).values('first_name')


User.objects.filter(first_name__endswith='수', country='경기도').values('balance')


from django.db.models import Q
User.objects.filter(Q(balance__gte=2000) | Q(age__lte=40)).count()


User.objects.filter(phone__startswith='010-').count()


user = User.objects.get(first_name='옥자', last_name='김')
user.country='경기도'
user.save()


User.objects.get(first_name='진호', last_name='백').delete()


User.objects.order_by('-balance').values('first_name', 'last_name', 'balance')[:4]


User.objects.filter(phone__contains='123', age__lt=30).values()


from django.db.models import Count
User.objects.filter(phone__startswith='010').values('country').annotate(Count('country'))


from django.db.models import Avg
User.objects.aggregate(Avg('age'))


from django.db.models import Avg
User.objects.filter(last_name='박').aggregate(Avg('balance'))


from django.db.models import Max
User.objects.filter(country='경상북도').aggregate(Max('balance'))


User.objects.filter(country='제주특별자치도').order_by('-balance').values('first_name')[0]