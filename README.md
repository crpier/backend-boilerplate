### TODO list
- Setup secrets in kubernetes
- Cache docker image on a volume or smth so that docker can get them from there 
instead of dockerhub. An image is like 500mb so it seems worth it. It takes
about a minute to just downloading lmao
- Make the docker image slimmer with multi stage builds 
- Add pre-commit maybe
- Don't use the root user anymore in mariadb
- Also certs man, you said you'd do it first thing this time
- Choose output port via config
