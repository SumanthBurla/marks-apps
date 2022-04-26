#!/usr/bin/env groovy

pipeline {
    agent {
        node { label 'default' }
    }
    
    parameters{
        string(name:'imageName_fromBuild', defaultValue: '', description:'Build source')
    }

    stages {
        // stage('Initialize'){ 
        //     steps{
        //         script{
        //             def dockerHome = tool 'myDocker'
        //             env.PATH = "${dockerHome}/bin:${env.PATH}"
        //             echo "Running ${env.BUILD_ID} job on ${env.JENKINS_URL}"
        //         }
        //     }
        // }
        stage('Pull image from Hub'){
            steps{
                echo "${params.imageName_fromBuild}"
                sh("docker pull ${params.imageName_fromBuild}")
            }
        }
        stage('Test run app'){
            steps{
                runApp()
            }
        }
    } 
    post {
        always {
            echo 'displays always --- this is always block from post-build section'
        }
        success {
            // deleteDir()
            echo '----- Job Succeeded -----'
            echo "app running on http://localhost:8083"
        } 
        failure {
            // deleteDir()
            echo 'displays when failure --- this is failure block from post-build section'
        }
    }
}

def runApp(){
    sh("docker run -d -p 8083:5000 ${params.imageName_fromBuild}")
}











        // stage('Deploy to GKE') {
        //     steps{
        //         sh "sed -i 's/hello:latest/marks-app:v${env.BUILD_ID}.0/g' deployment.yaml"
        //         sh('cat deployment.yaml')
        //         // step([$class: 'KubernetesEngineBuilder', projectId: env.PROJECT_ID, clusterName: env.CLUSTER_NAME, location: env.LOCATION, manifestPattern: 'deployment.yaml', credentialsId: env.CREDENTIALS_ID, verifyDeployments: true])
        //         //     withKubeConfig([credentialsId: env.CREDENTIALS_ID,
        //         //     caCertificate: '<ca-certificate>',
        //         //     serverUrl: '<api-server-address>',
        //         //     contextName: '<context-name>',
        //         //     clusterName: env.CLUSTER_NAME,
        //         //     namespace: 'default'
        //         //     ]) {
        //         // sh 'kubectl apply -f deployment.yaml' 
        //     }
        // }
        //         PROJECT_ID = 'future-silicon-342405'
        // CLUSTER_NAME = 'cluster-0'
        // LOCATION = 'us-central1-c'
        // CREDENTIALS_ID = 'k8s-jenkins'