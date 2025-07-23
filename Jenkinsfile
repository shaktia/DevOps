pipeline{
    agent any

    environment{
        Build_Dir="Build"
    }

    stages{
        stage('clone'){
            steps{
                echo 'cloning'
                git 'https://github.com/shaktia/DevOps.git'
            }
        }

        stage('build'){
            steps{
                sh '''
                mkdir -p $Build_Dir
                echo 'this is a build artifact' > $Build_Dir/output.txt

                '''
            }
        }

        stage('test'){
            steps{
                echo 'running test'
                sh '''
                if grep -q "artifact" $Build_Dir/output.txt ;then
                 echo 'test pass'
                else
                 echo 'tst fails'
                fi

                '''
            }
        }

        stage('archive'){
            steps{
                echo 'archiving artifact'
                archiveArtifacts artifacts: "$Build_Dir/output.txt" , fingerprint: true

            }
        }
    }

    post{
        success{
            echo 'Build comleted successfully'
        }

        failure{
            echo 'Build failed'
        }
    }
}
