pipeline {
  agent none
  stages {
    stage('Build dev image') {
      agent {
          kubernetes {
              yaml '''
apiVersion: v1
kind: Pod
spec:
  containers:
  - name: docker
    image: docker:19.03.1-dind
    securityContext:
      privileged: true
    resources:
      limits:
        cpu: 1
        memory: 1Gi
      requests:
        cpu: 0.5
        memory: 500Mi
'''
              defaultContainer 'docker'
            }
        }
      environment {
        registry = "tiannaru/whisper"
        registryCredential = 'dockertoken'
      }
      steps {
        script {
          sh "docker pull tiannaru/whisper:latest-dev"
          dockerImage = docker.build registry + ":latest-dev", "-f build/dockerfiles/Dockerfile --build-arg INSTALL_DEV=true --cache-from tiannaru/whisper:latest-dev ."
          docker.withRegistry('https://index.docker.io/v1/', registryCredential) {
            dockerImage.push()
          }
        }
      }
    }
    stage('Code analysis') {
      agent {
          kubernetes {
              yaml '''
spec:
  containers:
  - name: whisper-dev
    image: tiannaru/whisper:latest-dev
    imagePullPolicy: Always
    command:
    - sleep
    args:
    - 99d
    resources:
      limits:
        cpu: 2
        memory: 1.6Gi
      requests:
        cpu: 1
        memory: 800Mi
              '''
              defaultContainer 'whisper-dev'
            }
        }
      steps {
        sh "poetry exec lint"
        }
    }
    stage('Build image') {
      agent {
          kubernetes {
              yaml '''
apiVersion: v1
kind: Pod
spec:
  containers:
  - name: docker
    image: docker:19.03.1-dind
    securityContext:
      privileged: true
    resources:
      limits:
        cpu: 1
        memory: 1Gi
      requests:
        cpu: 0.5
        memory: 500Mi
'''
              defaultContainer 'docker'
            }
        }
      environment {
        registry = "tiannaru/whisper"
        registryCredential = 'dockertoken'
      }
      steps {
        script {
          // God I just hate jenkins. If this is what modern software development
          // looks like I'm writing my mcdonalds aplication form right now
          dockerImage = docker.build registry + ":latest", "-f build/dockerfiles/Dockerfile --build-arg INSTALL_DEV=true --cache-from tiannaru/whisper:latest ."
          docker.withRegistry('https://index.docker.io/v1/', registryCredential) {
            dockerImage.push()
          }
        }
      }
    }
    stage('Component tests') {
      agent {
          kubernetes {
              yaml '''
spec:
  containers:
  - name: whisper
    image: tiannaru/whisper:latest
    imagePullPolicy: Always
    command:
    - sleep
    args:
    - 99d
    resources:
      limits:
        cpu: 1
        memory: 1Gi
      requests:
        cpu: 0.5
        memory: 500Mi
              '''
              defaultContainer 'whisper'
            }
        }
      steps {
        sh "poetry run pytest ."
        }
      }
    stage('Deployment: Staging') {
      agent {
        label 'python-ci'
      }
      steps {
        // Workaround because kubectl doesn't do things in order and the 
        // namespace doesn't exist when the deployment is applied
        sh "kubectl apply -f deploy/kubernetes/namespace.yaml"
        sh "kubectl apply -f deploy/kubernetes/"
      }
    }
  }
}
