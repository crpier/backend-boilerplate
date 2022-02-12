pipeline {
  agent none
  stages {
    stage('Deployment: Staging') {
      agent {
        label 'python-ci'
      }
      steps {
        sh "kubectl apply -f deploy/kubernetes/"
      }
    }
    stage('Code analysis') {
      agent {
        label 'python-ci'
        }
      stages {
        stage('Code analysis: black') {
          steps {
            catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
              sh "black --check backend"
            }
          }
        }
        stage('Code analysis: flake8') {
          steps {
            catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
              sh "flake8 backend"
            }
          }
        }
        stage('Code analysis: pylint') {
          steps {
            catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
              sh "pylint backend"
            }
          }
        }
        stage('Code analysis: pydocstyle') {
          steps {
            catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
              sh "pydocstyle backend"
            }
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
  }
}
