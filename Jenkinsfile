#!/usr/bin/env groovy

pipeline {
    agent {
        node { label 'jenkins2' }
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
        // stage('Test-Flask-app'){
        //     steps{
        //         runApp()
        //     }
        // }
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
        stage('Deploy to GKE') {
            steps{
                sh "sed -i 's/hello:latest/marks-app:v${env.BUILD_ID}.0/g' deployment.yaml"
                sh('cat deployment.yaml')
                step([$class: 'KubernetesEngineBuilder', projectId: env.PROJECT_ID, clusterName: env.CLUSTER_NAME, location: env.LOCATION, manifestPattern: 'deployment.yaml', credentialsId: env.CREDENTIALS_ID, verifyDeployments: true])
            }
        }
    }
    post {
        always {
            sh('docker logout')
            echo 'displays always --- this is always block from post-build section'
        }
        success {
            // deleteDir()
            echo '----- Job Succeeded -----'
            echo "app running on http://localhost:8082"
            echo "https://hub.docker.com/repository/docker/${IMAGE_NAME}"
        }
        failure {
            // deleteDir()
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
