pipeline {
    agent any 
    
    stages{
        stage('Clone'){
            steps{
                echo 'cloning code'
                git 'https://github.com/shaktia/DevOps.git'
            }
        }

        stage('Build'){
            steps{
                echo 'Building the project'
            }
        }

        stage('Test'){
            steps{
                echo 'Testing the project'
            }
        }

        stage('Deploy'){
            steps{
                echo 'Deploying'
            }
        }
        

    }
}