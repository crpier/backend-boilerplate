pipeline {
  agent none
  stages {
    stage('Build dev image') {
      agent {
          kubernetes {
              yaml '''
apiVersion: v1
kind: Pod
spec:
  containers:
  - name: docker
    image: docker:19.03.1-dind
    securityContext:
      privileged: true
'''
              defaultContainer 'docker'
            }
        }
      environment {
        registry = "tiannaru/whisper"
        registryCredential = 'dockertoken'
      }
      steps {
        script {
          sh "docker pull tiannaru/whisper:latest-dev"
          dockerImage = docker.build registry + ":latest-dev", "-f build/dockerfiles/Dockerfile --build-arg INSTALL_DEV=true --cache-from tiannaru/whisper:latest-dev ."
          docker.withRegistry('https://index.docker.io/v1/', registryCredential) {
            dockerImage.push()
          }
        }
      }
    }
    stage('Code analysis') {
      agent {
          kubernetes {
              yaml '''
spec:
  containers:
  - name: whisper-dev
    image: tiannaru/whisper:latest-dev
    command:
    - sleep
    args:
    - 99d
              '''
              defaultContainer 'whisper-dev'
            }
        }
      steps {
        // We have to install this again because we cannot run the job
        // in the folder where the virtualenv was created, and thus the
        // hash that makes up the name of the venv won't be the same, 
        // so we simply can't use it.
        /* sh "poetry install --no-root" */

        sh "ls -la /usr/local/bin"
        sh "poetry config --list"
        sh "poetry run poetry exec lint"
        }
    }
    stage('Build image') {
      agent {
          kubernetes {
              yaml '''
apiVersion: v1
kind: Pod
spec:
  containers:
  - name: docker
    image: docker:19.03.1-dind
    securityContext:
      privileged: true
'''
              defaultContainer 'docker'
            }
        }
      environment {
        registry = "tiannaru/whisper"
        registryCredential = 'dockertoken'
      }
      steps {
        script {
          // God I just hate jenkins. If this is what modern software development
          // looks like I'm writing my mcdonalds aplication form right now
          dockerImage = docker.build registry + ":latest", "-f build/dockerfiles/Dockerfile --build-arg INSTALL_DEV=true --cache-from tiannaru/whisper:latest ."
          docker.withRegistry('https://index.docker.io/v1/', registryCredential) {
            dockerImage.push()
          }
        }
      }
    }
    stage('Component tests') {
      agent {
          kubernetes {
              yaml '''
spec:
  containers:
  - name: whisper
    image: tiannaru/whisper:latest
    command:
    - sleep
    args:
    - 99d
              '''
              defaultContainer 'whisper'
            }
        }
      steps {
        // The same workaround as above. We'll do this for every new image
        // This is what giving up looks like. Jenkins is STUBBORNLY insisting
        // on running in a "workspace/whisper_main" folder for some inane
        // reason that probably didn't even MAKE SENSE in 1984 when they
        // put together 3 plugins that don't care for each other
        // and called it an "automation server"
        sh "poetry install --no-root --no-dev"

        sh "poetry run pytest ."
        }
      }
    stage('Deployment: Staging') {
      agent {
        label 'python-ci'
      }
      steps {
        // Workaround because kubectl doesn't do things in order and the 
        // namespace doesn't exist when the deployment is applied
        sh "kubectl apply -f deploy/kubernetes/namespace.yaml"
        sh "kubectl apply -f deploy/kubernetes/"
      }
    }
  }
}
