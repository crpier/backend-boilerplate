pipeline {
  agent {
      label 'python-ci'
    }
  stages {
    // stage('Setup') {
    //   checkout scm
    // }
    stage('CI: Code analysis') {
      stages {
        stage('black') {
          steps {
            sh "black --check backend"
          }
        }
        stage('flake8') {
          steps {
            sh "flake8 backend"
          }
        }
        stage('pylint') {
          steps {
            sh "pylint backend"
          }
        }
        stage('pydocstyle') {
          steps {
            sh "pydocstyle backend"
          }
        }
      }
    }
  }
}
