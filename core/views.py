from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import LeagueNews, Club, League, Comment, Match
from django.utils import timezone
from .forms import ContactForm, CommentForm
from django.core.mail import send_mail, BadHeaderError
from django.db.models import Q

# Create your views here.
def home(request):
    league = League.objects.all()
    latest_news = LeagueNews.objects.filter(publication_date__lte=timezone.now()).order_by('-publication_date')[:20]
    return render(request, 'core/index.html', {'league':league, 'latest_news':latest_news})



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form':form})

def openleague(request, pk):
    league = League.objects.get(pk=pk)
    news = league.news.filter(publication_date__lte=timezone.now()).order_by('-publication_date')[:20]
    return render(request, 'core/openleague.html', {'league':league,'news':news})

def opennews(request, pk):
    league = League.objects.get(pk=pk)
    news = league.news.filter(publication_date__lte=timezone.now()).order_by('-publication_date')
    return render(request, 'core/opennews.html', {'news':news,'league':league})

def newsdetail(request, pk):
    league = League.objects.all()
    news = get_object_or_404(LeagueNews,pk=pk)
    return render(request, 'core/newsdetail.html',{'news':news, 'league':league})

def leaguerank(request, pk):
    league = League.objects.get(pk=pk)
    cl = league.club.all()
    clubs = sorted(cl,reverse=True, key= lambda t: t.total_points)
    return render(request, 'core/leaguerank.html', {'clubs': clubs, 'league':league})


def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, from_email, message,['omarkadytt@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('core:successcontact')
    return render(request, 'core/contactus.html', {'form':form})


def successcontact(request):
    return render(request, 'core/success.html')

def add_comment_to_news(request, pk):
    news = get_object_or_404(LeagueNews, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():# is_valid() method that check whether entered data is valid or not
            comment = form.save(commit=False)
            comment.leaguenews = news
            comment.save()
            return redirect('core:newsdetail', pk=news.pk)
    else:
        name = request.user.username
        form = CommentForm(initial={'author': name})
    return render(request, 'core/add_comment_to_news.html', {'form':form})

def clubpage(request, pk):
    club = get_object_or_404(Club, pk=pk)
    news = club.news.filter(publication_date__lte = timezone.now()).order_by('-publication_date')[:20]
    return render(request, 'core/clubpage.html', {'club':club, 'news':news})


def clubnews(request, pk):
    club = get_object_or_404(Club, pk=pk)
    news = club.news.filter(publication_date__lte = timezone.now()).order_by('-publication_date')
    return render(request, 'core/clubnews.html', {'club':club, 'news':news})


def openallclubs(request, pk):
    league = League.objects.get(pk=pk)
    clubs = league.club.all()
    return render(request, 'core/openallclubs.html', {'clubs':clubs, 'league':league})


def leaguematchs(request, pk):
    league = get_object_or_404(League, pk=pk)
    matchs = league.match.all().order_by('play_date')
    return render(request, 'core/leaguematchs.html', {'league':league, 'matchs':matchs})


def clubmatchs(request, pk):
    club = get_object_or_404(Club, pk=pk)
    matchs = Match.objects.filter(Q(club_local = pk)|Q(club_visitor = pk)).order_by('play_date')
    return render(request, 'core/clubmatchs.html', {'matchs':matchs, 'club':club})