pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Vipul-0722/jenkins_starter.git'
            }
        }
        stage('Build') {
            steps {
                sh 'echo Building app...'
                sh 'python3 app.py'
            }
        }
        stage('Test') {
            steps {
                sh 'echo Running tests...'
                sh 'python3 -m unittest test_app.py'
            }
        }
    }
}
