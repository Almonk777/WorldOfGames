pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Build') {
            steps {
                script {
                    docker.build('myapp:1.0', '.')
                }
            }
        }
        
        stage('Run') {
            steps {
                script {
                    docker.image('myapp:1.0').withRun('-p 8777:80 -v $(pwd)/dummy_Scores.txt:/app/Scores.txt') {
                        sleep 5
                    }
                }
            }
        }
        
        stage('Test') {
            steps {
                sh 'python e2e.py'
            }
        }
        
        stage('Finalize') {
            steps {
                script {
                    docker.image('myapp:1.0').stop()
                    docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials') {
                        docker.image('myapp:1.0').push()
                    }
                }
            }
        }
    }
    
    post {
        always {
            docker.image('myapp:1.0').stop()
        }
    }
}

