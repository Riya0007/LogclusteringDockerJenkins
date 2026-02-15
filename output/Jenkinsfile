pipeline {
    agent any

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
                sh "docker build -t $IMAGE_NAME ."
            }
        }

        stage('Run Clustering') {
            steps {
                sh "docker run --rm $IMAGE_NAME"
            }
        }

        stage('Archive Output') {
            steps {
                archiveArtifacts artifacts: 'output/**', fingerprint: true
            }
        }
    }
}
