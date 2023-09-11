
def index(request):
    return render(request, 'main/index.html')

def main(request):
    return render(request, 'main/main.html')


def questions(request):
    return render(request, 'main/question.html')
def questions2(request):
    return render(request, 'main/question2.html')
def questions3(request):
    return render(request, 'main/question3.html')
def questions4(request):
    return render(request, 'main/question4.html')
def questions5(request):
    return render(request, 'main/question5.html')
def questions6(request):
    return render(request, 'main/question6.html')
def questions7(request):
    return render(request, 'main/question7.html')



def question(request):
    return render(request, 'main/question.html')

def result(request):
    return render(request, 'main/result.html')

def test(request):
    return render(request, 'main/test.html')


from .models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login



from django.contrib.auth import authenticate, login

def login_register(request):
    if request.method == 'POST':
        if 'register' in request.POST:  # 회원가입 요청인 경우
            name = request.POST['name']
            phone_number = request.POST['phone_number']

            # 중복 여부 체크
            if User.objects.filter(name=name).exists():
                return render(request, 'main/login.html', {'message': '이미 존재하는 사용자입니다.'})

            # 사용자 생성
            user = User.objects.create_user(name=name, phone_number=phone_number)
            user.save()

            # 회원가입 성공 시 로그인 처리
            login(request, user)

            # 회원가입 및 로그인 성공 시 리다이렉트
            return redirect('index')  # or redirect('main:index')

        elif 'login' in request.POST:  # 로그인 요청인 경우
            login_name = request.POST['login_name']
            login_phone_number = request.POST['login_phone_number']

            user = authenticate(request, name=login_name, password=login_phone_number)
            if user is not None:
                login(request, user)
                # 로그인 성공 시 리다이렉트
                return redirect('index')  # or redirect('main:index')
            else:
                # 로그인 실패 시 처리할 내용
                return render(request, 'main/login.html', {'message': '로그인에 실패하였습니다.'})

    return render(request, 'main/login.html')


from django.shortcuts import render
from .models import UserInfo, User

def survey_form_submit(request):
    if request.method == 'POST':
        # POST 요청으로부터 데이터를 가져옴
        name = request.POST.get('name')

        q1 = request.POST.get('q1')

        # UserInfo 모델을 사용하여 데이터를 저장
        survey = UserInfo(q1=q1)
        usr = User(name=name)
        usr.save()
        survey.save()
        # 필요한 경우 다른 필드에 대한 데이터도 수집 및 저장

    return render(request, 'main/result.html')
