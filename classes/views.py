from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import contactus


# Create your views here.


from django.http import HttpResponse
from .models import *
from django.core.mail import send_mail
def contactpagecall(request):
    return render(request, 'contact.html')
# views.py
from django.shortcuts import redirect
from .models import contactus  # Ensure proper import

def contactlogic(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        comment = request.POST.get('comment')

        # Save data to the database using the ContactUs model
        contactus.objects.create(
            firstname=firstname,
            lastname=lastname,
            email=email,
            comment=comment
        )

        # Send email confirmation
        send_mail(
            'Thank you for your feedback!',
            f'Hello {firstname} {lastname},\n\nThank you for reaching out. We have received your comments:\n"{comment}". We will get back to you soon.\n\nBest regards,\nTeam Fluentia',
            'thummagantijayanthraj@gmail.com',  # Sender's email address
            [email],  # Recipient's email address
            fail_silently=False,
        )

        messages.success(request, "Thank you for your feedback!")
        # Redirect to base1.html (ensure 'base1' is correctly defined in URLs)
        return redirect('base1')



from django.shortcuts import render, redirect


from django.shortcuts import render, redirect
from django.contrib import messages  # For success messages

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import OnlineClass, OnlineClassRegistration

@login_required
def online_classes(request):
    classes = OnlineClass.objects.all()
    registered_classes = OnlineClassRegistration.objects.filter(user=request.user).values_list('online_class_id', flat=True)
    return render(request, 'online_classes.html', {
        'classes': classes,
        'registered_classes': registered_classes
    })

@login_required
def register_online_class(request):
    if request.method == 'POST':
        class_title = request.POST.get('class_title')
        try:
            online_class = OnlineClass.objects.get(title=class_title)
            if OnlineClassRegistration.objects.filter(user=request.user, online_class=online_class).exists():
                messages.info(request, "You are already registered for this online class.")
            else:
                OnlineClassRegistration.objects.create(user=request.user, online_class=online_class)
                messages.success(request, f"You have successfully registered for {online_class.title}.")
        except OnlineClass.DoesNotExist:
            messages.error(request, "Invalid class selected.")
    return redirect('online_classes')




from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def course_registration(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        courses = request.POST.getlist('courses')  # Get selected courses as list

        # Store the data (for now, just print it)
        print(f"Name: {name}, Email: {email}, Courses: {courses}")

        # Redirect to a confirmation or success page
        return redirect('success')

    # Pre-fill form with user details
    user = request.user
    return render(request, 'course_registration.html', {
        'username': user.username,
        'email': user.email,
    })

def success(request):
    return redirect('base1')

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Course, CourseRegistration

@login_required
def courses(request):
    courses = Course.objects.all()
    registered_courses = CourseRegistration.objects.filter(user=request.user).values_list('course_id', flat=True)
    return render(request, 'courses.html', {
        'courses': courses,
        'registered_courses': registered_courses
    })


@login_required
def register_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if CourseRegistration.objects.filter(user=request.user, course=course).exists():
        messages.info(request, "You are already registered for this course.")
    else:
        CourseRegistration.objects.create(user=request.user, course=course)
        messages.success(request, f"You have successfully registered for {course.title}.")
    return redirect('courses')


# views.py
@login_required
def course_material(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    # Check if the user is registered for the course
    if not CourseRegistration.objects.filter(user=request.user, course=course).exists():
        messages.error(request, "You must register for this course to access its content.")
        return redirect('courses')  # Redirect to the courses list if not registered

    return render(request, 'course_material.html', {'course': course})


from django.shortcuts import render
from .models import Faculty

def about(request):
    return render(request, 'about.html')

def schedules(request):
    return render(request, 'schedules.html')

def faculties(request):
    course = request.GET.get('course')
    faculties = Faculty.objects.filter(course=course) if course else []
    return render(request, 'faculties.html', {'faculties': faculties})



from django.shortcuts import render


# Predefined responses based on user input
import re

def get_response(user_input):
    # List of responses related to language learning and platform features
    responses = {
        'exercises': "Use interactive exercises like fill-in-the-blank, matching games, and sentence creation to reinforce what you've learned.",
        'practice': "Regular practice is essential for language learning. Dedicate time each day to review vocabulary, practice grammar, and engage in conversation.",
        'online class': "Join our online classes to practice with a teacher and fellow learners. These classes provide live interaction and focused learning.",
        'course registration': "Register for courses by visiting the ‘Course Registration’ section. Choose the course that best fits your needs and start learning today.",
        'track': "Track your progress through the dashboard. View completed lessons, quizzes, and badges earned to see how far you've come.",
        'practice exercises': "Use our practice exercises to reinforce what you've learned. These exercises include vocabulary, grammar, and speaking tasks.",
        'group sessions': "Participate in group sessions to practice with other learners and receive feedback from instructors.",
        'feedback': "Use the platform’s feedback features to get insights on your exercises and assignments. It helps identify areas to improve.",
        'courses': "Explore our range of 4 Foreign language courses, designed to take you from beginner to advanced level. Choose a course based on your current skill level and goals.",
        'assignments': "Complete assignments to practice your language skills, such as writing exercises, quizzes, and speaking tasks. Check your submissions for detailed feedback.",
        'lessons': "Access lessons covering various topics and skill levels, from beginner to advanced. Lessons include video tutorials, practice exercises, and quizzes.",
        'chatbot': "Use our chatbot to get quick answers to your language learning questions. It’s here to help you 24/7.",
        'certificates': "Earn certificates upon completion of courses and achievements. These certificates validate your learning progress and can be shared with potential employers.",
        'profile': "Update and manage your profile to track your learning progress, preferences, and achievements. Set goals and milestones to stay motivated.",
        'community': "Join the community forum to connect with fellow learners, share tips, and practice conversation in a supportive environment.",
        'review': "Leave a review for a course or instructor. Your feedback helps us improve our platform and supports other learners in making informed decisions.",
        'vocabulary': "Expand your vocabulary with our word lists, flashcards, and quizzes. Focus on the most common words and phrases for practical use.",
        'grammar': "Master grammar rules through detailed explanations, practice exercises, and quizzes. Our platform covers everything from basic to advanced grammar.",
        'audio lessons': "Listen to audio lessons to practice pronunciation and listening skills. Record your own voice to compare it with native speakers.",
        'live chat': "Use live chat to get immediate help with your language questions. Connect with instructors or other learners online.",
        'feedback survey': "Complete our feedback survey to share your thoughts on the platform and suggest improvements. Your input helps us enhance your experience."
    }

    # Preprocess user input to lowercase and remove extra spaces
    user_input = user_input.lower().strip()

    # Check if any keyword matches the user input using regex
    for key, response in responses.items():
        if re.search(key, user_input):
            return response

    return "Sorry, I couldn't understand that. Please try again."




# Chatbot view to handle user input
def chatbot_view(request):
    bot_response = ''
    user_input = ''

    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')
        if user_input:
            bot_response = get_response(user_input)
        else:
            bot_response = "Please type a message."

    return render(request, 'chat.html', {'bot_response': bot_response, 'user_input': user_input})



from django.shortcuts import render, redirect
from .models import Assignment

def assignments_list(request):
    assignments = Assignment.objects.all()
    return render(request, 'assignments_list.html', {'assignments': assignments})

def add_assignment(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        Assignment.objects.create(
            title=title,
            description=description,
            due_date=due_date
        )
        return redirect('assignments_list')
    return render(request, 'add_assignment.html')

# You might want a detail view for assignment details
def assignment_detail(request, pk):
    assignment = Assignment.objects.get(pk=pk)
    return render(request, 'assignment_detail.html', {'assignment': assignment})



# views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse

def exercise_selection(request):
    return render(request, 'exercise_selection.html')

def vocabulary_exercise(request):
    if request.method == 'POST':
        word = request.POST.get('word')
        # Process the word (e.g., check against database)
        return redirect('exercise_selection')
    return render(request, 'exercise_selection.html')

def submit_vocabulary(request):
    if request.method == 'POST':
        word = request.POST.get('word')
        # Process the word (e.g., check against database)
        return redirect('exercise_selection')
    return HttpResponse("Invalid request method.", status=405)

def grammar_exercise(request):
    if request.method == 'POST':
        sentence = request.POST.get('sentence')
        # Process the sentence (e.g., check grammar)
        return redirect('exercise_selection')
    return render(request, 'exercise_selection.html')

def submit_grammar(request):
    if request.method == 'POST':
        sentence = request.POST.get('sentence')
        # Process the sentence (e.g., check grammar)
        return redirect('exercise_selection')
    return HttpResponse("Invalid request method.", status=405)

def speaking_exercise(request):
    if request.method == 'POST':
        response = request.POST.get('sentence')
        # Process the response (e.g., record and store)
        return redirect('exercise_selection')
    return render(request, 'exercise_selection.html')

def submit_speaking(request):
    if request.method == 'POST':
        response = request.POST.get('sentence')
        # Process the response (e.g., record and store)
        return redirect('exercise_selection')
    return HttpResponse("Invalid request method.", status=405)



