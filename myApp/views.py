from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, Http404, request
from django.template import loader
from .models import allCourses,details,ProfileCreate

# Create your views here.

def Courses(request):
    ac = allCourses.objects.all()
    template = loader.get_template('myApp/Courses.html')
    Context = {
        'ac':ac,
    }
    return HttpResponse(template.render(Context,request))


def details(request,course_id):
    try:
        course = allCourses.objects.get(pk = course_id)
    except allCourses.DoesNotExist:
        raise Http404("Course not available")
    return render(request,'myApp/details.html',{'course':course} )

def yourchoice(request,course_id):
    course = get_object_or_404(allCourses,pk=course_id)
    try:
        selected_ct = course.details_set.get(pk=request.POST['choice'])
    except (KeyError,allCourses.DoesNotExist):
        return render(request, 'myApp/detail.html',{
            'course':course,
            'error_messgae':"select a valid option"
        })
    else:
        selected_ct.your_choice=True
        selected_ct.save()
        return render(request,'myApp.html',{'course':course})




