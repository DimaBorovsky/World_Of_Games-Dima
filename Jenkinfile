pipeline {
    agent any

    environment {
        DOCKER_IMAGE_NAME = 'dimaborovsky12/python:3-alpine'
        CONTAINER_NAME = 'gifted_mclean'
        TEST_CONTAINER_NAME = 'gifted_mclean'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm 'https://github.com/DimaBorovsky/World_Of_Games-Dima.git'
            }
        }

        stage('Build') {
            steps {
                script {
                    sh 'docker build -t ${gifted_mclean}'
                    
            }
        }

        stage('Run') {
            steps {
                script {
                    sh '''
                        docker run -d --name ${CONTAINER_NAME} \
                        -p 8777:8777 \
                        -v $(pwd)/Scores.txt:/app/Scores.txt ${gifted_mclean}           
                        '''
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    sh 'python3 e2e.py'
                }
            }
        }

        stage('Finalize') {
            steps {
                script {
                    sh 'docker stop ${gifted_mclean} && docker rm ${gifted_mclean}'
                    sh 'docker push ${python-3:alpine}'
                }
            }
        }
    }

    post {
        always {
            script {
                sh 'docker container prune -f'
                sh 'docker image prune -f'
            }
        }
    }
