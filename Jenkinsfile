podTemplate(containers: [
    containerTemplate(name: 'python-ci', image: 'tiannaru/python-ci'),
  ]) {

    node(POD_LABEL) {
        stage('Code analysis') {
            // git scm
            container('python-ci') {
                stage('Code analysis') {
                  sh "ls -la"
                }
            }
        }

    }
}
