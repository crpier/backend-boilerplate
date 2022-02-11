podTemplate(containers: [
    containerTemplate(name: 'python-ci', image: 'tiannaru/python-ci', command: 'sleep', args: '99d'),
]) {
  node(POD_LABEL) {
    stage('Continuous integration') {
      container('python-ci') {
        stage('Setup') {
          checkout scm
        }
        stage('CI: Code analysis') {
          sh "ls -la"
        }
      }
    }
  }
}
