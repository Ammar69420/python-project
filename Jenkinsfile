pipeline {
    agent any

    stages {
        stage('Declarative: Checkout SCM') {
            steps {
                checkout scm  // Checkout your source code from GitHub
            }
        }

        stage('Check Docker Containers') {
            steps {
                script {
                    // Check existing Docker containers
                    bat 'docker ps -a'
                }
            }
        }

        stage('Clone Repository') {
            steps {
                script {
                    // Clone the repository again if necessary
                    git branch: 'master', url: 'https://github.com/Ammar69420/python-project.git'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image using the Dockerfile in the repository
                    bat 'docker build -t ammarrr03/python-project .'
                }
            }
        }

        stage('Login to Docker Hub') {
            steps {
                script {
                    // Use Jenkins credentials to securely login to Docker Hub
                    withCredentials([usernamePassword(credentialsId: '1234', passwordVariable: 'Am123456@', usernameVariable: 'ammarrr03')]) {
                     bat 'echo %DOCKER_PASSWORD% | docker login -u %DOCKER_USERNAME% --password-stdin'
}
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    // Push the Docker image to Docker Hub
                    bat 'docker push ammarrr03/python-project'
                }
            }
        }

        stage('Post Actions') {
            steps {
                script {
                    // Clean up unused Docker resources
                    bat 'docker system prune -f'
                }
            }
        }
    }

    post {
        failure {
            // Handle failure post-build actions
            echo "The build has failed. Please check the logs for details."
        }
        success {
            // Handle success post-build actions
            echo "The build was successful."
        }
    }
}
