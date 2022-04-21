#!/usr/bin/env groovy

pipeline {
    agent {
        node { label 'jenkins2' }
    }
    
    environment {
        ABC = 1
        GCP_ACCESS_TOKEN = "credentials('jenkins')"
        IMAGE_NAME="gcr.io/marks-app"
        IMAGE_TAG="v1.0"
        jenkins="gcr.io/marks-app"
    }
    parameters {
        string(name: 'STATEMENT', defaultValue: 'ls /', description: 'What should I say?')
    }
    stages {
        stage('Initialize'){
            steps{
            script{
                def dockerHome = tool 'myDocker'
                env.PATH = "${dockerHome}/bin:${env.PATH}"
            }}
        }
        stage('env-variables') {
            environment { 
                DEBUG_FLAGS = '-g'
            }
            steps {
                echo "Running ${env.BUILD_ID} on ${env.JENKINS_URL}"
                sh 'printenv'
                echo "${GCP_ACCESS_TOKEN}"
                sh('echo ${STATEMENT}')
            }
        }
        stage('Build') {
            steps{
                script{
                sh('docker build -t $IMAGE_NAME:$IMAGE_TAG .')
                // docker.build jenkins + ":$BUILD_NUMBER" 
                // sh('docker pull jenkins/jenkins:latest')
                echo "Build complete..."
                sh('docker images')
            }
        }}
        stage('Hello-world-stage') {
            steps{
                sh 'echo $ABC' 
                echo 'Hello world!'
            }
        }
        stage('Execution-stage') {            
            steps{
                sh 'echo "Both files vm.tf and version.tf files have $(expr $(wc -w README.md | awk \'{ print $1 }\') + $(wc -w .gitignore | awk \'{ print $1 }\') ) words..."'
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
            echo 'displays when failure --- this is failure block from post-build section'
        }
    }
}

