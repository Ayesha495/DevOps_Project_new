pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = 'c5b75660-79c2-4cef-a9c5-a93aa9ca652d' 
        IMAGE_NAME = 'nabihanasir/calculator'         
        IMAGE_TAG = 'ver1'
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
                        // Note: Passing passwords in CLI can show in logs; 
                        // consider 'docker login --password-stdin' for better security.
                        bat "docker login -u %DOCKER_USER% -p %DOCKER_PASS%"
                        bat "docker push ${IMAGE_NAME}:${IMAGE_TAG}"
                    }
                }
            }
        }
    } // End of stages

    post {
        success {
            echo "Pipeline completed successfully ✅"
        }
        failure {
            echo "Pipeline failed ❌"
        }
    }
}
