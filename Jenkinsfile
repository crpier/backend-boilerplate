podTemplate(containers: [
    containerTemplate(name: 'python-ci', image: 'jenkins/inbound-agent:4.3-4', command: 'sleep', args: '99d'),
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
