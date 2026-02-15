pipeline {

    agent {
        docker {
            image 'docker:24-dind'
            args '-v /var/run/docker.sock:/var/run/docker.sock'
        }
    }

    environment {
        IMAGE_NAME = "log-clustering:latest"
    }

    triggers {
        cron('H 2 * * *')   // Runs daily at 2 AM
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh """
                docker build -t $IMAGE_NAME .
                """
            }
        }

        stage('Run Clustering') {
            steps {
                sh """
                mkdir -p output
                docker run --rm \
                -v \$(pwd)/output:/app/output \
                $IMAGE_NAME
                """
            }
        }

        stage('Archive Output') {
            steps {
                archiveArtifacts artifacts: 'output/**', fingerprint: true
            }
        }
    }
}
