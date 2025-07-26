pipeline {
    agent any

    environment {
        IMAGE_NAME = "shaktia04/demo"
        BUILD_TAG = "${BUILD_NUMBER}"
        CONTAINER_NAME = "jenkins-deploy-demo"
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

        stage('Deploy Container') {
            steps {
                echo '🚀 Deploying Docker Container...'
                script {
                    // Stop and remove existing container (if running)
                    sh """
                        docker ps -a --format '{{.Names}}' | grep -w $CONTAINER_NAME && docker rm -f $CONTAINER_NAME || echo 'No existing container'
                        docker run -d --name $CONTAINER_NAME $IMAGE_NAME:$BUILD_TAG tail -f /dev/null
                    """
                }
            }
        }
    }

    post {
        success {
            echo "✅ Docker build completed: $IMAGE_NAME:$BUILD_TAG"
        }
        failure {
            echo "❌ Docker build failed!"
        }
    }
}
