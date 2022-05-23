#!/usr/bin/env groovy

pipeline{
    agent any
    stages{
        stage('clone repo'){
            steps{
                git branch: 'temp', url: 'https://github.com/SumanthBurla/marks-apps.git'
            }
        }
        stage('Build'){
            steps{
                sh 'docker build -t sam:v11.1 .'
            }
        }
        stage('run'){
            steps{
                sh 'docker run -d -p 8088:5000 sam:v11.1'
            }
        }
    }
}
