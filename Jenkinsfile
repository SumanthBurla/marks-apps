#!/usr/bin/env groovy

pipeline {
    agent {
        node { label 'jenkins2' }
    }
    
    environment {
        IMAGE_NAME="sburla/marks-app"
        DOCKERHUB_CREDENTIALS=credentials('dockerHub-cred')
    }

    stages {
        stage('Initialize'){
            steps{
                script{
                    def dockerHome = tool 'myDocker'
                    env.PATH = "${dockerHome}/bin:${env.PATH}"
                    echo "Running ${env.BUILD_ID} job on ${env.JENKINS_URL}"
                }
            }
        } 
        stage('Build') {
            steps{
                buildImage()
        }}
        stage('random-Execution-stage') {            
            steps{
                sh 'echo "Both files app.py and version.tf files have $(expr $(wc -w app.py | awk \'{ print $1 }\') + $(wc -w Jenkinsfile | awk \'{ print $1 }\') ) words..."'
            }
        }
        stage('Test-Flask-app'){
            steps{
                runApp()
            }
        }
        stage('Dockerhub-login'){
            steps{
                sh 'docker login -u $DOCKERHUB_CREDENTIALS_USR -p $(echo $DOCKERHUB_CREDENTIALS_PSW )'
                // sh 'res=$(echo $?)'
                // sh 'echo $res'
            }
        }
        stage('Push to hub'){
            steps{
               pushImage()
            }
        }
    }
    post {
        always {
            sh('docker logout')
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