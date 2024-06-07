from django.shortcuts import render, redirect
from django.conf import settings
import requests
from .models import GithubApp
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Create your views here.
@csrf_exempt
def login(request):
    """Redirects to the github Authorization page"""
    github_auth = f"https://github.com/login/oauth/authorize?client_id={settings.GITHUB_CLIENT_ID}&scope=repo"
    return redirect(github_auth)

@csrf_exempt  
def callback(request):
    """Returns the names of both the public repos and private repos and saves them to
    the database"""
    code = request.GET.get('code')
    token_url = "https://github.com/login/oauth/access_token"
    token_data = {
        'client_id': settings.GITHUB_CLIENT_ID,
        'client_secret': settings.GITHUB_CLIENT_SECRET,
        'code': code
    }

    headers = {'Accept': 'application/json'}
    token_resp = requests.post(token_url, data=token_data, headers=headers).json()
    token = token_resp.get('access_token')

    repos = "https://api.github.com/user/repos"
    headers = {
        'Authorization': f"token {token}",
        'Accept': 'application/vnd.github.v3+json'
    }

    resp = requests.get(repos, headers=headers).json()
    public_repos = []
    private_repos = []
    for a_repo in resp:
        if a_repo['private']:
            private_repos.append(a_repo['name'])
        else:
            public_repos.append(a_repo['name'])
        GithubApp.objects.update_or_create(
            name=a_repo['name'], 
            defaults={
                'public_repo': not a_repo['private'],
                'private_repo': a_repo['private']
            }
        )
    response = {
        'public_repos': public_repos,
        'private_repos': private_repos
    }
    return JsonResponse(response, status=200)

@csrf_exempt
def get_repos(request):
    """Returns the names of both the public repos and private repos"""
    repos = GithubApp.objects.all()
    public_repos = []
    private_repos = []
    for repo in repos:
        if repo.public_repo:
            public_repos.append(repo.name)
        else:
            private_repos.append(repo.name)
    response = {
        'public_repos': public_repos,
        'private_repos': private_repos
    }
    return JsonResponse(response, status=200)
