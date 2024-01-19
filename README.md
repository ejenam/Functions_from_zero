# Functions_from_zero

curl -X POST 'https://noahgift-functions-from-zero-r7g59wcx6x-8080.githubpreview.dev/wiki' \
-H 'Accept: application/json' \
-H 'Content-Type: application/json' \
-d '{"name": "Microsoft"}'

https://glowing-space-enigma-q6gg7j9qxgg2rrp-8080.app.github.dev/docs#/default/scrape_story_wiki_post

### Build container
touch Dockerfile
docker build .
docker image ls

### Run container
docker run -p 127.0.0.1:8080:8080 2520d033d4df

###### open a new bash
curl http://0.0.0.0:8080

### invoke post request
bash invoke.sh