pipeline {
    agent any

    environment {
        IMAGE_NAME = "shaktia04/demo"
        BUILD_TAG = "${BUILD_NUMBER}"
    }

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/shaktia/DevOps.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    echo "Building Docker Image..."
                    sh "docker build -t ${IMAGE_NAME}:${BUILD_TAG} ."
                }
            }
        }

        stage('Docker Push (Optional)') {
            when {
                expression { return env.DOCKER_PUSH == 'true' }
            }
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh '''
                      echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                      docker push $IMAGE_NAME:$BUILD_TAG
                    '''
                }
            }
        }
    }

    }
    post{
        sucess{
            echo "Docker build completed : $IMAGE_NAME:$BUILD_TAG"
        }
    }

