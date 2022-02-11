pipeline {
  agent none
  stages {
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
  stage('Unit tests') {
    agent {
        kubernetes {
            yaml '''
              spec:
              containers:
              - name: app
                image: tiannaru/whisper:latest
                command:
                - sleep
                args:
                - 99d
            '''
          }
      }
    steps {
        sh "pytest ."
      }
    }
  }
}
