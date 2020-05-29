import sendgrid
import os
from django.conf import settings
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, UserProfileUpdateForm, StudentRegistrationForm, ChildProfileUpdateForm, ActivityCreationForm, GuardianRegisterForm
from .models import child, activity, newsletter, guardian
from django.core.mail import send_mail
from sendgrid.helpers.mail import *
from celery import shared_task

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,
                'Your account has been created! You are now able to Log In', "alert alert-success alert-dismissible")
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'usersProfile/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = UserProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.extendeduser)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,
                'Your account has been updated', "alert alert-success alert-dismissible")
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = UserProfileUpdateForm(instance=request.user.extendeduser)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'usersProfile/profile.html', context)


@login_required
def enrol(request):
    return render(request, 'usersProfile/enrol.html', {'title': "Enrol"})


class ChildRegister(TemplateView):
    template_name = 'usersProfile/studentProfile.html'

    def get(self, request):
        form = StudentRegistrationForm()
        guardian_form = GuardianRegisterForm()
        context = {
            'c_form': form,
            'g_form': guardian_form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = StudentRegistrationForm(request.POST)
        guardian_form = GuardianRegisterForm(request.POST)
        if form.is_valid() and guardian_form.is_valid():
            instance = form.save(commit=False)
            guardianName = guardian_form.cleaned_data.get('guardian_name')
            relationGuardian = guardian_form.cleaned_data.get('relation_guardian')
            phoneNum = guardian_form.cleaned_data.get('phone_num')
            new_guardian = guardian(guardian_name=guardianName, relation_guardian=relationGuardian,
                                    phone_num=phoneNum)
            new_guardian.save()
#            guardian_instance = guardian_form.save(commit=False)
            instance.user = request.user
            user = request.user
            instance.parent_name = User.objects.get(username=user).username
            instance.parent_id = User.objects.get(username=user).pk
            instance.guardian_name_id = new_guardian.id
            instance.save()
            form = StudentRegistrationForm()
            guardian_form = GuardianRegisterForm()
            return redirect('/')

        # args = {'form': form, }
        context = {
            'c_form': form,
            'g_form': guardian_form
        }
        return render(request, self.template_name, context)


def display_child_list(request):
    user = request.user
    name = user.username
#    print(name)
    user_id = User.objects.get(username=user).pk
    type(User.objects.get(username=user).pk)
#    print(user_id)
    children = child.objects.all()
#    child_sel = request.GET["dropdown"]
    for ch in children:
        print(ch)
        guard = ch.guardian_name_id
        print("**********************")
        print(guard)
        print("**********************")
    print('Selected Child')
#    print(child_sel)
    args = {'children': children, 'primary_key': user,
            'user_id': user_id, 'name': name}
    for ch in children:
        # if name == ch.parent_name:
        if user_id == ch.user_id:
            print(ch.parent_name)
            print(ch.child_name)
#        if int(ch.parent_id) == int(user_id):
#            print(ch.parent_id)
#            print(ch.child_name)
#            print(ch.parent_name)
        else:
            pass
#    print(children)
    return render(request, 'usersProfile/displayChildList.html', args)
#    result = request.GET["dropdown"]
    print("selected *****************")
    print(result)


def display_child_profile1(request, pk=None):
    print("reached student.views.display_child_profile")
    child_list = child.objects.all()
    if pk:
        selected_child = child.objects.get(pk=pk)
        print(selected_child, pk, selected_child.child_name)

#    print(name)
    args = {'child': selected_child}
    return render(request, 'usersProfile/displayChildProfile.html', args)


def display_child_profile(request, pk=None):
    template_name = 'usersProfile/updateChildProfile.html'
    child_list = child.objects.all()
    if pk:
        selected_child = child.objects.get(pk=pk)

    selected_child = child.objects.get(pk=pk)
    print("*******************************************************8")
    print(selected_child.child_name)
    print(selected_child.child_age)

    if request.method == 'POST':
        u_form = ChildProfileUpdateForm(
            request.POST, instance=request.user)
#            p_form = UserProfileUpdateForm(
#                request.POST, request.FILES, instance=request.user.extendeduser)
        if u_form.is_valid():
            u_form.save()
            messages.success(request,
                'Your account has been updated', "alert alert-success alert-dismissible")
            return redirect('profile')
    else:
        u_form = ChildProfileUpdateForm(instance=request.user)

    context = {
        'u_form': u_form
    }
    return render(request, 'usersProfile/displayChildProfile.html', context)


def activity_creation(request):
    teacher_list = User.objects.filter(is_staff=True)
    if request.method == 'POST':
        activity_form = ActivityCreationForm(request.POST)
        if activity_form.is_valid():
            teacherName = activity_form.cleaned_data.get('teacher_name')
            print("************** Teacher name", teacherName)
            listOfChildren = activity_form.cleaned_data.get('children_list')
            activityName = activity_form.cleaned_data.get('activity_name')
            activityDesc = activity_form.cleaned_data.get(
                'activity_description')
            activityDate = activity_form.cleaned_data.get(
                'activity_Date')
            activityDuration = activity_form.cleaned_data.get(
                'activity_duration')
            print(activityName, activityDate, activityDuration)
            new_activity = activity(teacher_name=teacherName, activity_name=activityName,
                                    activity_description=activityDesc, activity_Date=activityDate, activity_duration=activityDuration)
            new_activity.save()

            for children in listOfChildren:
                new_activity.children_list.add(children)
            messages.success(request,
                'Activity created successfully', "alert alert-success alert-dismissible")
            return redirect('enrol')

    else:
        activity_form = ActivityCreationForm()

    return render(request, 'usersProfile/activityCreationForm.html', {'activity_form': activity_form})


def send_signup_mail1(email, signup_message):
    subject = "Thank You for Joining Kindergarten"
    from_email = settings.EMAIL_HOST_USER
    to_email = email
    #signup_message = """Welcome to KinderGarten !!!!!!"""
    send_mail(subject=subject, message=signup_message, from_email=from_email,
              recipient_list=[to_email], fail_silently=False)

@shared_task
def send_signup_mail(email, signup_message):
    sg = sendgrid.SendGridAPIClient('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')
    from_email = Email("beerinder@mysite.com")
    to_email = To(email)
    subject = "Thank You for Joining Kindergarten"
    content = Content("text/plain", "You are onboarded, Now login and enjoy a simpler life!")
    mail = Mail(from_email, to_email, subject, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)
    #signup_message = """Welcome to KinderGarten !!!!!!"""

def display_child_activity_list(request, pk):
    template_name = 'usersProfile/display_child_activity_list.html'
    child_list = child.objects.all()
    if pk:
        selected_child = child.objects.get(pk=pk)

    selected_child = child.objects.get(pk=pk)
    child_name = selected_child.child_name
    act_list = activity.objects.filter(
        children_list__child_name=child_name)
    if not act_list:
        messages.success(request,
                'No activity assigned to your child', "alert alert-success alert-dismissible")
        return redirect('display_child_list')
    else:
        args = {'child': selected_child, 'activity': act_list}
        return render(request, 'usersProfile/displayChildActivityList.html', args)


def types_of_activity(request):
    activity_display_options = {
        "Select_Activity",
        "Select_Child"
    }
    children_list = child.objects.all()
    selected_option = request.POST.get('dropdown')
    querySet = activity.objects.none()
    if(selected_option == "All_Children"):
        querySet = activity.object.all()
    args = {'child': children_list,
            'displayOptions': activity_display_options, 'query_set': querySet}
    querySet = activity.objects.none()
    return render(request, 'usersProfile/displayActivity.html', args, selected_option)


def delete_activity(request):
    if request.method == 'POST':
        selected_option = request.POST.get('dropdown')

        selected_Activity = activity.objects.filter(id=selected_option)
        print(selected_Activity)
        selected_Activity.delete()
        #act = activity.objects.filter(activity_name=selected_option)
        #for a in act:
        #    if a.activity_name == selected_option:
        #        activityID = a.id
        #        print("****ID, name", activityID, a.activity_name)
        #        act = activity.objects.filter(id=activityID).delete()
        #        print(" Before Deleting Activity", act)
        #        print("**********************", act)
                # act.delete()

        # act.delete()

        list_of_activity = activity.objects.all().order_by('-activity_Date')
        # return redirect('enrol')

    else:
        print("************* in else")
        list_of_activity = activity.objects.all().order_by('-activity_Date')

    args = {'query_set': list_of_activity}

    return render(request, 'usersProfile/deleteActivity.html', args)


def display_activity(request):
    activity_display_options = {
        "Select_Activity",
        "Select_Child"
    }
    children_list = child.objects.all()
    selected_option = request.POST.get('dropdown')
    querySet = activity.objects.none()
    if(selected_option == "All_Children"):
        querySet = activity.object.all()
    args = {'child': children_list,
            'displayOptions': activity_display_options, 'query_set': querySet}
    querySet = activity.objects.none()
    return render(request, 'usersProfile/displayActivity.html', args, selected_option)


def display_options_for_activity(request):
    if request.method == 'POST':
        selected_option = request.POST.get('dropdown')
        print("******* BEER *******", selected_option, type(selected_option))
        option = str('Display_All_Activities')
        print("******* BEER *******", selected_option, type(selected_option), type(option))
#        if(selected_option != str(option)):
        if(str(selected_option) == str(option)):
            print("**************** Into Display_All_Activities")
        list_of_activity = activity.objects.all()
    else:
        print("************* in else")
        list_of_activity = activity.objects.all()

    activity_display_options = {
        "Select_Activity",
        "Display_All_Activities"
    }
    args = {'query_set': list_of_activity, 'displayOptions': activity_display_options,}

#    return render(request, 'usersProfile/deleteActivity.html', args)
    return render(request, 'usersProfile/displayOptionsForActivity.html', args)
    #return redirect('display_child_list')

def newsletter_signup(request):
    if request.method == 'POST':
        user_email = str(request.POST.get('Email'))
        if newsletter.objects.filter(email=user_email).exists():
            messages.warning(request,
                'Your Email Already exists in our database', "alert alert-warning alert-dismissible")
        else:
            newsletter.objects.create(email=user_email)
            messages.success(request,
                'Your email has been submitted to the database', "alert alert-success alert-dismissible")
            signup_message = """Your email has been subscribed successfully"""
            send_signup_mail(user_email, signup_message)
        return redirect('/')

    return redirect('/')
