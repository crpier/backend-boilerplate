pipeline {
  agent {
    kubernetes {
      label 'myLabel'
      idleMinutes 1
      yaml '''
apiVersion: v1
kind: Pod
metadata:
  labels:
    some-label: some-label-value
spec:
  containers:
  - name: jnlp
    image: jenkins/inbound-agent:alpine-jdk11
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
