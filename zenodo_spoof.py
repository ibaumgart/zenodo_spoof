import requests

# Fill these in...
repo = "<user>/<reponame>"
token = "<access token from webhook page in repo>"

headers = {"Accept": "application/vnd.github.v3+json"}

repo_response = requests.get(f"https://api.github.com/repos/{repo}", headers=headers)
release_response = requests.get(f"https://api.github.com/repos/{repo}/releases", headers=headers)

latest_release = release_response.json()[0]

payload = {"action": "published", "release": latest_release, "repository": repo_response.json()}

submit_response = requests.post(
    f"https://zenodo.org/api/hooks/receivers/github/events/?access_token={token}",
    json=payload
)

print(submit_response)