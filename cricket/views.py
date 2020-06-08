from django.shortcuts import render
from django.views.generic.list import ListView
from cricket.models import Team,Player,Points,Match
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.
class TeamListView(ListView):
    model = Team
    template_name = 'index.html'


def detail(request,team_id):
    team = Team.objects.get(id= team_id)
    player = Player.objects.filter(team=team_id)
    return render(request,'detail_team.html',{'players':player,'team':team})

def points(request):
    points = Points.objects.all()
    return render(request,'points.html',{'points':points})

def matches(request):
    matches = Match.objects.all()
    return render(request,'matches.html',{'matches':matches})
