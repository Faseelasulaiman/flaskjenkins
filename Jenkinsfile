pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh 'python3 -m pytest'
            }
        }

        stage('Build') {
            steps {
                sh 'python3 -m py_compile app.py'
            }
        }
    }
}