pipeline {
  agent none
  stages {
    stage('Build image') {
      agent {
          kubernetes {
              yaml '''
                spec:
                  containers:
                  - name: dind
                    image: docker:1.11
                    command:
                    - cat
                    tty: true
                    volumeMounts:
                    - name: dockersock
                      mountPath: /var/run/docker.sock
                  volumes:
                  - name: dockersock
                  hostPath:
                    path: /var/run/docker.sock
              '''
              defaultContainer 'dind'
            }
        }
      environment {
        registry = "tiannaru/whisper"
        registryCredential = 'dockertoken'
      }
      steps {
        script {
          dockerImage = docker.build registry + ":latest"
          docker.withRegistry('', registryCredential) {
            dockerImage.push()
          }
        }
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
  }
}
