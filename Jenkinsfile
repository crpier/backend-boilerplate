podTemplate(containers: [
    containerTemplate(name: 'python-ci', image: 'tiannaru/python-ci', command: 'sleep', args: '99d'),
  ]) {

    node(POD_LABEL) {
        stage('Code analysis') {
            // git scm
            container('maven') {
                stage('Build a Maven project') {
                  sh "ls -la"
                }
            }
        }

    }
}
