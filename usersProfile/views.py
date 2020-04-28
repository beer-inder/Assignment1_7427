from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, UserProfileUpdateForm, StudentRegistrationForm, ChildProfileUpdateForm
from .models import child


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Your account has been created! You are now able to Log In')
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
            messages.success(
                request, f'Your account has been updated')
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
    #    if request.method == 'POST':
    #        form = StudentRegistrationForm(request.POST, instance=request.user)
    #        if form.is_valid():
    #            form.save()
    #            username = form.cleaned_data.get('child_name')
    #            messages.success(
    #                request, f'Your account has been created!')
    #            user = request.user
    #            user_id = User.objects.get(username=user).pk
    #            user_name = User.objects.get(username=user).username
    #            print('Reached')
    #            print(user_id)
    #            print(user_name)
    #            return redirect('/')

    #   else:
    #        form = StudentRegistrationForm(instance=request.user)
    # return render(request, 'student/enrol.html', {'form': form})
    return render(request, 'usersProfile/enrol.html', {'title': "Enrol"})


@login_required
def register_child1(request):
    #    return HttpResponse('<h1>Home</h1>')
    if request.method == 'POST':
        form = StudentRegistrationForm(
            request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            instance = form.save(commit=False)
            username = form.cleaned_data.get('child_name')
            messages.success(
                request, f'Your account has been created!')
            user = request.user
            user_id = User.objects.get(username=user).pk
            user_name = User.objects.get(username=user).username
            child.parent_name = user_name
            instance.user = request.user
            instance.parent_name = User.objects.get(username=user).username
            instance.parent_id = int(User.objects.get(username=user).pk)
            instance.save()
            print(instance.parent_name)
            print(instance.parent_id)
            print('Reached')
            print(user_id)
            print(user_name)
            return redirect('/')
    else:
        form = StudentRegistrationForm(instance=request.user)
    print("reached student.views.register")
    return render(request, 'usersProfile/studentProfile.html', {'form': form})


class ChildRegister(TemplateView):
    template_name = 'usersProfile/studentProfile.html'

    def get(self, request):
        form = StudentRegistrationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            user = request.user
            instance.parent_name = User.objects.get(username=user).username
            instance.parent_id = User.objects.get(username=user).pk
            instance.save()
            print(instance.parent_name)
            print(instance.parent_id)
            # child_name = form.cleaned_data['instance']
            form = StudentRegistrationForm()
            return redirect('/')

        # args = {'form': form, }
        return render(request, self.template_name, {'form': form})


def display_child_list(request):
    print("reached student.views.display_child_list")
    user = request.user
    name = user.username
#    print(name)
    user_id = User.objects.get(username=user).pk
    type(User.objects.get(username=user).pk)
    user_id_u = user.id
#    print(user_id)
    children = child.objects.all()
#    child_sel = request.GET["dropdown"]
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
            messages.success(
                request, f'Your account has been updated')
            return redirect('profile')
    else:
        u_form = ChildProfileUpdateForm(instance=request.user)

    context = {
        'u_form': u_form
    }
    return render(request, 'usersProfile/displayChildProfile.html', context)
