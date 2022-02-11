podTemplate(containers: [
    containerTemplate(name: 'python-ci', image: 'tiannaru/python-ci', command: 'sleep', args: '99d'),
  ]) {

    node(POD_LABEL) {
        stage('Continuous integration') {
            // git scm
            container('python-ci') {
                stage('CI: Code analysis') {
                  sh "ls -la"
                }
            }
        }

    }
}
