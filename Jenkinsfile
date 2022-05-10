#!/usr/bin/env groovy

pipeline {
    agent {
        node { label 'default' }
    }
    
    environment {
        PROJECT_ID = 'future-silicon-342405'
        CLUSTER_NAME = 'demo-cluster'
        LOCATION = 'us-central1-a'
        CREDENTIALS_ID = 'future-silicon-342405'
        K8S_CONFIG= 'kubernetes-config'
    }

    stages {
            stage('List pods') {
                steps{
                withKubeConfig([credentialsId: env.K8S_CONFIG]) {
                    sh 'curl -LO "https://storage.googleapis.com/kubernetes-release/release/v1.20.5/bin/linux/amd64/kubectl"'  
                    sh 'chmod u+x ./kubectl'  
                    sh './kubectl get pods'
                }
                }
            }
        stage('Deploy to GKE') {
            steps{
                sh '''
                    sed -i 's/hello:latest/marks-app:v13.0/g' deployment.yaml
                    cat deployment.yaml
                    echo $PATH
                    ls /usr/local/bin
                    /usr/local/bin/kubectl
                    kubectl
                '''
                step([$class: 'KubernetesEngineBuilder', projectId: env.PROJECT_ID, clusterName: env.CLUSTER_NAME, location: env.LOCATION, manifestPattern: 'deployment.yaml', credentialsId: env.CREDENTIALS_ID, verifyDeployments: true])
                //     withKubeConfig([credentialsId: env.CREDENTIALS_ID,
                //     caCertificate: '<ca-certificate>',
                //     serverUrl: '<api-server-address>',
                //     contextName: '<context-name>',
                //     clusterName: env.CLUSTER_NAME,
                //     namespace: 'default'
                //     ]) {
                // sh 'kubectl apply -f deployment.yaml' 
            }
        }       
    } 
    post {
        always {
            echo 'displays always --- this is always block from post-build section'
        }
        success {
            echo '----- Job Succeeded -----'
        } 
        failure {
            deleteDir()
            echo 'displays when failure --- this is failure block from post-build section'
        }
    }
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