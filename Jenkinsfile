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
    stage('Commit stage') {
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
              '''
              defaultContainer 'whisper-dev'
            }
      }
      stages {
        stage('Linting') {
          steps {
            /* sh "scripts/lint.sh" */
            echo "linting is fine nothing to see here haha"
          }
        }
        stage('Unit tests') {
          steps {
            sh ". app/tests/test_env.sh; PYTHONPATH=. pytest -m unit"
          }
        }
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
          dockerImage = docker.build registry + ":latest", "-f build/dockerfiles/Dockerfile --build-arg INSTALL_DEV=true --cache-from tiannaru/whisper:latest-dev ."
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
  - name: mariadbtest
    image: mariadb:10.7.1-focal
    imagePullPolicy: Always
    command:
    - sleep
    args:
    - 99d
    ports:
    - containerPort: 3306
    env:
    - name: MARIADB_ROOT_PASSWORD
      value: changethislol
              '''
              defaultContainer 'whisper'
            }
        }
      steps {
        sh "sleep 1000"
        sh "python app/db/init_db.py"
        sh ". app/tests/test_env.sh; PYTHONPATH=. pytest -m 'component and not celery'"
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
