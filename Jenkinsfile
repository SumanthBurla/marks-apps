#!/usr/bin/env groovy

pipeline{
    agent {
        label 'ubuntu'
    }
    stages{
        stage('clone repo'){
            steps{
                git branch: 'temp', url: 'https://github.com/SumanthBurla/marks-apps.git'
                sh "docker version" 
                sh 'whoami'
                sh 'hostname'
            }
            post{
                 success{
                    echo "changing to temp branch"
                    echo "building image noew...."
                }
            }
        }
        stage('Build'){
            steps{
                sh 'docker build -t sam:v11.1 .'
            }
            post{
                success{
                    echo "images build sucessfully"
                    echo "showing images...."
                }
            }
        }
        stage('images'){
            steps{
                sh 'docker images'
            }
            post{
                 success{
                    echo "showed images...."
                }
            }
        }
    }
}
