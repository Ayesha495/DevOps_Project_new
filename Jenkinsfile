pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = 'dockercred' 
        IMAGE_NAME = 'ayesha495/calculator-app'         
        IMAGE_TAG = '3-25-25.2'
    }

    stages {

        stage('Pull code from GitHub') {
            steps {
                echo "Cloning repository..."
                git branch: 'main', url: 'https://github.com/Ayesha495/DevOps_Project_new.git'
            }
        }

        stage('Build Docker image') {
            steps {
                echo "Building Docker image..."
                script {
                    bat "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ."
                }
            }
        }

       stage('Push Docker image to Docker Hub') {
        steps {
        echo "Logging into Docker Hub and pushing image..."
        script {
            withCredentials([usernamePassword(
                credentialsId: "${DOCKERHUB_CREDENTIALS}",
                usernameVariable: 'DOCKER_USER',
                passwordVariable: 'DOCKER_PASS'
            )]) {
                bat "docker login -u %DOCKER_USER% -p %DOCKER_PASS%"
                bat "docker push ${IMAGE_NAME}:${IMAGE_TAG}"
            }
        }
    }
}
        }

    }

    post {
        success {
            echo "Pipeline completed successfully ✅"
        }
        failure {
            echo "Pipeline failed ❌"
        }
    }
}
