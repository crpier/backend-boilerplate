pipeline {
  agent none
  stages {
    stage('Unit tests') {
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
          sh "pwd"
          sh "ls -la"
          sh "whoami"
          sh "hostname"
          sh "ls -la /usr/local/bin"
          sh "/usr/local/bin/pytest ."
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
  }
}
