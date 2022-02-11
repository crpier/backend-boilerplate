pipeline {
  agent {
      label 'python-ci'
    }
  stages {
    // stage('Setup') {
    //   checkout scm
    // }
    stage('CI: Code analysis') {
      steps {
        sh "black --check backend"
      }
    }
  }
}
