pipeline {
    agent {
        docker {
            image 'python:3.9-slim'  // Docker image for Jenkins agent
            args '-v /var/run/docker.sock:/var/run/docker.sock'  // Mount Docker socket
        }
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm  // Checkout the latest code from SCM (Git)
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image inside the container
                    sh 'docker build -t ammarrr03/python-project .'
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: '1234', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                    // Login and push the Docker image to Docker Hub
                    sh 'docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD'
                    sh 'docker push ammarrr03/python-project'
                }
            }
        }
    }

    post {
        success {
            echo 'Build and push successful!'
        }
        failure {
            echo 'Build failed. Check logs.'
        }
    }
}
