"""Assignment1_7420_WebApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from usersProfile import views as user_views
from usersProfile.views import ChildRegister

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('enrol/', user_views.enrol, name='enrol'),
    path('enrol_student/', user_views.ChildRegister.as_view(), name='enrol_student'),
    # path('update_student_profile/', user_views.update_student_profile,
    #    name='update_student_profile'),
    path('display_child_list/', user_views.display_child_list,
         name='display_child_list'),
    # path('display_child_activity_list/(?P<pk>\d+)/', user_views.display_child_activity_list,
    #     name='display_child_activity_list'),
    path('<int:pk>/display_child_activity_list/', user_views.display_child_activity_list,
         name='display_child_activity_list'),
    path('display_child_activity_list/', user_views.display_child_activity_list,
         name='display_child_activity_list'),
    path('activity_creation/', user_views.activity_creation,
         name='activity_creation'),
    path('delete_activity/', user_views.delete_activity,
         name='delete_activity'),
    path('display_activity/', user_views.display_activity,
         name='display_activity'),
    path('types_of_activity/', user_views.types_of_activity,
         name='types_of_activity'),
#    path('display_options_for_activity/', user_views.display_options_for_activity,
#         name='display_options_for_activity'),
    path('display_child_profile/(?P<pk>\d+)/', user_views.display_child_profile,
         name='display_child_profile'),
    path('newsletter_signup/', user_views.newsletter_signup,
         name='newsletter_signup'),
    path('login/', auth_views.LoginView.as_view(template_name='usersProfile/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='usersProfile/logout.html'), name='logout'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view
         (template_name='usersProfile/password_reset.html'),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view
         (template_name='usersProfile/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/(?P<uidb64>[0-9A-Za-z])-(?P<token>,+)/',
         auth_views.PasswordResetConfirmView.as_view
         (template_name='usersProfile/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view
         (template_name='usersProfile/password_reset_complete.html'),
         name='password_reset_complete'),
    #path('password-reset/', PasswordResetView, name='password_reset'),
    #path('password-reset/done/', PasswordResetDoneView, name='password_reset_done'),
    path('', include('e_assist.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),




    ] + urlpatterns
