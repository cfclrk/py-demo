pipeline {
    agent { docker { image 'python:3.9.0' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
                sh 'pip install -U pip setuptools'
                sh 'pip install .[dev]'
            }
        }
        stage('test') {
            steps {
                sh 'make test'
            }
        }
    }
}
