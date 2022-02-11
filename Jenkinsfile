pipeline {
  agent {
      label 'python-ci'
    }
  stages {
    stage('Code analysis') {
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
