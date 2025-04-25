pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'jagadhish3/movie-recommendation' // your Docker Hub image name
        DOCKER_TAG = 'latest'
        DOCKER_CREDENTIALS_ID = 'jagadhish3-docker' // Jenkins credentials ID
    }

    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/Jagadhish3/Devops_Proj.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE}:${DOCKER_TAG}")
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', "${DOCKER_CREDENTIALS_ID}") {
                        docker.image("${DOCKER_IMAGE}:${DOCKER_TAG}").push()
                    }
                }
            }
        }

        stage('Cleanup Local Docker Image') {
            steps {
                sh "docker rmi ${DOCKER_IMAGE}:${DOCKER_TAG} || true"
            }
        }
    }

    post {
        success {
            echo '✅ Deployment pipeline completed successfully.'
        }
        failure {
            echo '❌ Deployment failed. Check the logs for details.'
        }
    }
}
