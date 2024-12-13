pipeline {
    agent any

    stages {
        stage('install_connection_verify') {
            steps {
                echo 'Hello World'
                sh 'java --version'
                sh 'python3 -V'
                sh 'docker version'
                git branch: 'master' , url: 'https://github.com/redashu/ashu-unisys-cicd.git'
                sh 'ls'
            }
        }
        // docker build 
        stage('building docker image'){
            steps {
                echo 'building docker image for selenium code'
                sh 'ls'
                sh 'docker build -t  ashuselenium:test2 . '
                sh 'docker images | grep -i ashuselenium'
            }
        }
        // selenium prerequiste 
        stage('selenium prerequsite test'){
            steps {
                echo 'checking google chrome version'
                sh 'google-chrome   --version'
                echo 'checking chromedriver version'
                sh 'chromedriver --version'
                echo 'location of chromedriver to use in python code'
                sh 'which chromedriver'
            }

        }
        // doing SAST in selenium python code 
        stage('using trivy scan in current code'){
            steps {
                echo 'checking trivy version'
                sh 'trivy -version'
                echo 'scanning the python code'
                sh 'trivy fs  .'
            }
        }
        // running python selenium in headless mode 
        stage('running selenium in headless mode'){
            steps {
                echo 'running python code for selenium headless'
                sh 'python3 automate.py'
                echo 'verify image png '
                sh 'ls '
            }
        }
    }
}