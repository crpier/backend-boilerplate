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
          sh "pwd"
          sh "whoami"
          sh "ls -la /root/.cache"
          sh 'echo "echo $PATH" > sc.sh'
          sh "chmod +x sc.sh"
          sh 'poetry run bash -c "./sc.sh"'
          sh "which poetry"
          sh "poetry --version"
          sh "/root/.local/bin/poetry run whoami"
          sh "/root/.local/bin/poetry run echo $PATH"
          sh "/root/.local/bin/poetry run ls -laR /root/.cache/pypoetry/virtualenvs/"
          sh "/root/.local/bin/poetry run which python"
          sh "/root/.local/bin/poetry run python -m mypy"
          sh "/root/.local/bin/poetry run scripts/lint.sh"
          sh "/root/.local/bin/poetry run mypy"
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
          sh "/usr/local/bin/pytest ."
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
          dockerImage = docker.build registry + ":latest", "-f build/dockerfiles/Dockerfile --build-arg INSTALL_DEV=true --cache-from tiannaru/whisper:latest ."
          docker.withRegistry('https://index.docker.io/v1/', registryCredential) {
            dockerImage.push()
          }
        }
      }
    }
    stage('Deployment: Staging') {
      agent {
        label 'python-ci'
      }
      steps {
        // Workaround because kubectl doesn't do things in order and the 
        // namespace doens't exist when the deployment is applied
        sh "kubectl apply -f deploy/kubernetes/namespace.yaml"
        sh "kubectl apply -f deploy/kubernetes/"
      }
    }
  }
}
