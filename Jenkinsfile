#!/usr/bin/env groovy

pipeline {
    agent {
        node { label 'jenkins2' }
    }
    
    environment {
        GCP_ACCESS_TOKEN = "credentials('jenkins')"
        IMAGE_NAME="gcr.io/marks-app"
    }
    // parameters {
    //     string(name: 'STATEMENT', defaultValue: 'ls /', description: 'What should I say?')
    // }
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
                // sh 'printenv'
                echo "${GCP_ACCESS_TOKEN}"
                sh('echo ${STATEMENT}')
            }
        }
        stage('Build') {
            steps{
                script{
                sh('docker build -t $IMAGE_NAME:v$BUILD_ID.0 .')
                echo "Build complete..."
                sh('docker images')
            }
        }}
        stage('Execution-stage') {            
            steps{
                sh 'echo "Both files app.py and version.tf files have $(expr $(wc -w app.py | awk \'{ print $1 }\') + $(wc -w .gitignore | awk \'{ print $1 }\') ) words..."'
            }
        }
        stage('Flask-runApp'){
            steps{
                sh('docker run -d -p 8083:5000 $IMAGE_NAME:v$BUILD_ID.0')
                echo "app running on http://localhost:8083"
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

