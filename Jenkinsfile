#!/usr/bin/env groovy

pipeline {
    agent {
        node { label 'jenkins2' }
    }
    
    environment {
        IMAGE_NAME="gcr.io/marks-app"
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
                buildImage($IMAGE_NAME)
            //     script{
            //     sh('docker build -t $IMAGE_NAME:v$BUILD_ID.0 .')
            //     echo "Build complete..."
            //     sh('docker images')
            // }
        }}
        stage('random-Execution-stage') {            
            steps{
                sh 'echo "Both files app.py and version.tf files have $(expr $(wc -w app.py | awk \'{ print $1 }\') + $(wc -w Jenkinsfile | awk \'{ print $1 }\') ) words..."'
            }
        }
        stage('Test-Flask-app'){
            steps{
                runApp(IMAGE_NAME)
            }
        }
        stage('Push to hub'){
            steps{
                echo "script TBD for pushing..."
            }
        }
    }
    post {
        always {
            echo 'displays always --- this is always block from post-build section'
        }
        success {
            deleteDir()
            echo 'displays when success --- this is success block from post-build section'
        }
        failure {
            deleteDir()
            echo 'displays when failure --- this is failure block from post-build section'
        }
    }
}

def buildImage(String imageName){
    sh('docker build -t $imageName:v$BUILD_ID.0 .')
    echo "Build complete..."
    sh('docker images')
}
def runApp(String imageName){
    sh('docker run -d -p 8083:5000 $imageName:v$BUILD_ID.0')
    echo "app running on http://localhost:8083"
}
