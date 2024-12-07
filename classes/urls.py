from django.urls import path
from . import views

urlpatterns = [

    path('courses/',views.courses, name = 'courses'),
    path('contactpagecall/',views.contactpagecall,name='contactpagecall'),
    path('contactlogic/',views.contactlogic,name='contactlogic'),
    path('about/', views.about, name='about'),
    path('faculties/', views.faculties, name='faculties'),
    path('schedules/', views.schedules, name='schedules'),
    path('chatbot_view/', views.chatbot_view, name='chatbot_view'),
    path('assignment_list/', views.assignments_list, name='assignments_list'),
    path('assignments/add/', views.add_assignment, name='add_assignment'),
    path('assignments/<int:pk>/', views.assignment_detail, name='assignment_detail'),
    path('online_classes/', views.online_classes, name='online_classes'),
    path('register_online_class/', views.register_online_class, name='register_online_class'),
    path('register_course/<int:course_id>/', views.register_course, name='register_course'),
    path('course_material/<int:course_id>/', views.course_material, name='course_material'),
    path('exercise_selection', views.exercise_selection, name='exercise_selection'),
    path('exercise/vocabulary/', views.vocabulary_exercise, name='vocabulary_exercise'),
    path('exercise/vocabulary/submit/', views.submit_vocabulary, name='submit_vocabulary'),
    path('exercise/grammar/', views.grammar_exercise, name='grammar_exercise'),
    path('exercise/grammar/submit/', views.submit_grammar, name='submit_grammar'),
    path('exercise/speaking/', views.speaking_exercise, name='speaking_exercise'),
    path('exercise/speaking/submit/', views.submit_speaking, name='submit_speaking'),
]
