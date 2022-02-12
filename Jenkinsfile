pipeline {
  agent none
  stages {
    stage('Code analysis') {
      agent {
        label 'python-ci'
        }
      steps {
          sh "scripts/lint.sh"
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
          sh "pwd"
          sh "ls -la"
          sh "whoami"
          dockerImage = docker.build registry + ":latest"
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
