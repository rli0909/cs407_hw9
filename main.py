import requests
import time

while True:
    r = requests.get("http://localhost:8080/api/posts")
    jsonData = r.json()

    for post in jsonData['posts']:
        print("title: " + post['title'])
        if 'post_anonymously' in post:
            print("post_anonymously: " + str(post['post_anonymously']))

    print("version: " + jsonData['version'])
    print("\n")

    time.sleep(3)
