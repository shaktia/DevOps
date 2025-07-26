pipeline {
    agent any

    environment {
        IMAGE_NAME = "shaktia04/demo"
        BUILD_TAG = "${BUILD_NUMBER}"
        CONTAINER_NAME = "jenkins-deploy-demo"
        REMOTE_HOST = "ec2-16-170-204-51.eu-north-1.compute.amazonaws.com"
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
                    sh """
                        docker ps -a --format '{{.Names}}' | grep -w $CONTAINER_NAME && docker rm -f $CONTAINER_NAME || echo 'No existing container'
                        docker run -d --name $CONTAINER_NAME $IMAGE_NAME:$BUILD_TAG tail -f /dev/null
                    """
                }
            }
        }

        stage('Remote Deploy on EC2') {
            steps {
                sshagent(['ec2-ssh-key']) {
                    sh """
                    ssh -o StrictHostKeyChecking=no ubuntu@$REMOTE_HOST '
                      docker rm -f $CONTAINER_NAME || true
                      docker pull $IMAGE_NAME:$BUILD_TAG
                      docker run -d --name $CONTAINER_NAME $IMAGE_NAME:$BUILD_TAG
                    '
                    """
                }
            }
        }
    }

    post {
        success {
            echo "✅ Docker build completed and container deplyed: ${IMAGE_NAME}:${BUILD_TAG}"
        }
        failure {
            echo "❌ Docker build & deployment failed!"
        }
    }
}
