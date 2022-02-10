pipeline {
  agent {
    kubernetes {
      label 'myLabel'
      idleMinutes 1
      yaml '''
apiVersion: v1
kind: Pod
metadata:
  namespace: jenkins-pods
  labels:
    some-label: some-label-value
spec:
  containers:
  - name: jnlp
    image: jenkins/jnlp:3.7-1-alpine
    args: 
    - ${computer.jnlpmac} ${computer.name}
    tty: true
'''
    }
  }
    stages {
        stage ('myStage') {
            steps {
                script {
                    echo "coucou"
                }
            }
        }
    }
}
