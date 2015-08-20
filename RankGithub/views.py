from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from RankGithub.models import Github
from RankGithub.utils import GithubClient


class GithubForm(forms.Form):
    url_1 = forms.CharField(label="Github Url 1", max_length=200)
    url_2 = forms.CharField(label="Github Url 2", max_length=200)

    gh_user = forms.CharField(label="Github Username", max_length=50)
    gh_pw = forms.CharField(label="Github Password", widget=forms.PasswordInput)


def get_store_info(url, user, pw):
    info = GithubClient(url, user, pw)
    results = info.fetch()

    repo = Github(name=results['name'], url=url, num_stars=results['stargazers_count'],
                  num_watchers=results['subscribers_count'], num_forks=results['forks_count'])

    return repo

# View of Index Page
def index(request):
    if request.POST:
        form = GithubForm(request.POST)

        if form.is_valid():
            url1 = form.cleaned_data['url_1']
            url2 = form.cleaned_data['url_2']
            gh_user = form.cleaned_data['gh_user']
            gh_pw = form.cleaned_data['gh_pw']

            git_1 = get_store_info(url1, gh_user, gh_pw)
            git_2 = get_store_info(url2, gh_user, gh_pw)

            return render(request, 'results.html', {'git_1': git_1, 'git_2': git_2})
        else:
            return render(request, 'index.html', {'form': form})
    else:
        form = GithubForm()

        return render(request, 'index.html', {'form':form})