pipeline {
    agent any  // This defines where the pipeline will run (on any available agent)

    environment {
        DOCKER_IMAGE = "python-project"  // Define the Docker image name
        DOCKERHUB_USERNAME = "ammarrr03" // Your DockerHub username
        DOCKERHUB_PASSWORD = credentials('1234')  // Jenkins credentials ID for DockerHub password
    }

    stages {
        stage('Check Docker Containers') {
            steps {
                script {
                    // Check Docker containers on the Jenkins agent (Windows version)
                    bat 'docker ps -a'
                }
            }
        }
        
        stage('Clone Repository') {
            steps {
                git 'https://github.com/Ammar69420/python-project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    bat 'docker build -t $DOCKERHUB_USERNAME/$DOCKER_IMAGE .'
                }
            }
        }
        
        stage('Login to Docker Hub') {
            steps {
                script {
                    bat "echo $DOCKERHUB_PASSWORD | docker login -u $DOCKERHUB_USERNAME --password-stdin"
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    bat 'docker push $DOCKERHUB_USERNAME/$DOCKER_IMAGE'
                }
            }
        }
    }

    post {
        always {
            // Clean up (optional)
            bat 'docker system prune -f'
        }
    }
}
