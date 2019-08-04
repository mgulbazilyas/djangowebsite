from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from .somewhere import SortHeaders
# Create your views here.
from schools.models import ProfessorData

LIST_HEADERS = (
    ("SChoool",None),
    ('Subject',None),
    ('Class Number',None),
    ('Class Size', None),
    ('First Name', 'first_name'),
    ('Last Name', 'last_name'),
    ('Email', None),
)
def index(request):
    user_list = ProfessorData.objects.all()
    page = request.GET.get('page', 1)
    order = request.GET.get('sort','school')
    print(order)

    paginator = Paginator(user_list, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return render(request,'schools/index.html',context={ 'users': users })

