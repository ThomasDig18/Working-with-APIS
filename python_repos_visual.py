import requests 

from plotly.graph_objs import Bar
from plotly import offline

#This is an API call and it stores the response 
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

#Store API response in a variable
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")

#Explore information about the repositories
repo_dicts = response_dict['items']
repo_names, stars = [], [] 
for repo_dict in repo_dicts:
	repo_names.append(repo_dict['name'])
	stars.append(repo_dict['stargazers_count'])

data = [{
	'type': 'bar',
	'x': repo_names,
	'y': stars,
}]

my_layout = {
	'title': 'Most-Starred Python Projects on GitHub',
	'xaxis': {'title': 'Repository'},
	'yaxis': {'title': 'Stars'},
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')

#Examine the first repository
repo_dict = repo_dicts[0]

print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
	print(f"Name: {repo_dict['name']}")
	print(f"Owner: {repo_dict['owner']['login']}")
	print(f"Stars: {repo_dict['stargazers_count']}")
	print(f"Repository: {repo_dict['html_url']}")
	print(f"Created: {repo_dict['created_at']}")
	print(f"Updated: {repo_dict['updated_at']}")
	print(f"Description: {repo_dict['description']}")