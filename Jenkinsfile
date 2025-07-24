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
    }
}
