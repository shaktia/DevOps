pipeline{
    agent any

    environment{
        IMAGE_NAME = "shaktia04/demo"
        BUILD_TAG = "${BUILD_NUMBER}"
    }

    stages{
        stage('clone'){
            steps{
                git 'https://github.com/shaktia/DevOps.git'
            }
        }

        stage('docker build'){
            steps{
                script{
                    echo "building docker image"
                    sh "docker build -t $IMAGE_NAME:$BUILD_TAG ."
                }
            }
        }
        
    }
}