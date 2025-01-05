pipeline {
    agent any  // This defines where the pipeline will run (on any available agent)

    environment {
        DOCKER_IMAGE = "python-project"  // Define the Docker image name
        DOCKERHUB_USERNAME = "ammarrr03" // Your DockerHub username
        DOCKERHUB_PASSWORD = credentials('dockerhub-password')  // Jenkins credentials ID for DockerHub password
    }

    stages {
        stage('Clone Repository') {
            steps {
                // Clone the repository from your version control system (Git, GitHub, etc.)
                git 'https://github.com/your/repository.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image
                    sh 'docker build -t $DOCKERHUB_USERNAME/$DOCKER_IMAGE .'
                }
            }
        }

        stage('Login to Docker Hub') {
            steps {
                script {
                    // Log in to Docker Hub
                    sh "echo $DOCKERHUB_PASSWORD | docker login -u $DOCKERHUB_USERNAME --password-stdin"
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    // Push the image to Docker Hub
                    sh 'docker push $DOCKERHUB_USERNAME/$DOCKER_IMAGE'
                }
            }
        }
    }
    
    post {
        always {
            // Clean up (optional)
            sh 'docker system prune -f'
        }
    }
}
