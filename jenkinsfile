pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sh './test.sh'
            }
        }
        
        stage('Tes'){
            steps{
                echo 'Testing....'
                sh 'echo "Tests passwed"'
            }
        }
        
         stage('Deploy') {
            steps {
                echo 'Test...'
                sh 'echo "Deployin.."'
            }
        }
    }
}
