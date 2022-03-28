# backend-boilerplate
Boilerplate for RESTful API written in python3.7 using FastAPI, leveraging MariaDB for storage, Celery for background tasks and HashiCorp Vault for secrets management.
Deployment is done with a Jenkins pipeline and the artifacts are Docker containers.
Made for the infrastructure setup in https://github.com/crpier/subsistence_infrastructure
Based on https://github.com/tiangolo/full-stack-fastapi-postgresql, but changed to use the only tech stack I really know.

## Usage
- create a new repository using this one as a template.
- rename all references to `backend-boilerplate`
- rename all references to `crpier`

### TODO list
- Make the docker image slimmer with multi stage builds or smth
- Add pre-commit maybe
- Choose output port via config
- create sa in manifests
