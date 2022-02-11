pipeline {
  agent {
    label 'python-ci'
  }
  stages {
    stage('Setup') {
      checkout scm
    }
    stage('CI: Code analysis') {
      sh "ls -la"
    }
  }
}
