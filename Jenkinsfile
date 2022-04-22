#!/usr/bin/env groovy

pipeline {
  agent {
    kubernetes {
      label 'marks-app'
      defaultContainer 'jnlp'
      yaml """
apiVersion: v1
kind: Pod
metadata:
labels:
  component: ci
spec:
  # Use service account that can deploy to all namespaces
  serviceAccountName: k8s-jenkins
  containers:
  - name: docker
    image: gcr.io/cloud-builders/docker
    command:
    - cat
    tty: true
  - name: kubectl
    image: gcr.io/cloud-builders/kubectl
    command:
    - cat
    tty: true
"""
}
  }
    
    environment {
        IMAGE_NAME="sburla/marks-app"
        DOCKERHUB_CREDENTIALS=credentials('dockerHub-cred')
        PROJECT_ID = 'future-silicon-342405'
        CLUSTER_NAME = 'cluster-0'
        LOCATION = 'us-central1-c'
        CREDENTIALS_ID = 'k8s-jenkins'
    }

    stages {
        stage('Build') {
            steps{
                container('docker') {
                    buildImage()
                }
            }
        }
        stage('Dockerhub-login'){
            steps{
                container('docker') {
                sh 'docker login -u $DOCKERHUB_CREDENTIALS_USR -p $(echo $DOCKERHUB_CREDENTIALS_PSW )'
                // sh 'res=$(echo $?)'
                // sh 'echo $res'
            }}
        }
        stage('Push to hub'){
            steps{
                container('docker') {
                pushImage()
                sh('docker logout')
            }}
        }
    }
    post {
        always {
            echo 'displays always --- this is always block from post-build section'
        }
        success {
            deleteDir()
            echo '----- Job Succeeded -----'
            echo "app running on http://localhost:8082"
            echo "https://hub.docker.com/repository/docker/${IMAGE_NAME}"
        }
        failure {
            deleteDir()
            echo 'displays when failure --- this is failure block from post-build section'
        }
    }
}

def buildImage(){
    sh('docker build -t $IMAGE_NAME:v$BUILD_ID.0 .')
    echo "Build complete..."
    sh('docker images')
}
def runApp(){
    sh('docker run -d -p 8082:5000 $IMAGE_NAME:v$BUILD_ID.0')
}

def pushImage(){
    sh('docker push $IMAGE_NAME:v$BUILD_ID.0')
    echo "----- ${IMAGE_NAME} pushed -----"
}
