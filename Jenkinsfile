pipeline{
    agent any

    stages{
        stage('clone'){
            steps{
                echo "cloning"
                git 'https://github.com/shaktia/DevOps.git'
            }
        }

        stage('build'){
            steps{
                echo 'building'
            
            }
        }

        stage('test'){
            steps{
                echo 'testing'
            }
        }

        stage('deploying'){
            steps{
                echo "deploying"
            }
        }
        
        stage('Finish'){
            steps{
                echo "finish"
            }
        }


    
    }
}