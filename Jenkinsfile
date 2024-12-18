pipeline {
    agent any

    triggers {
        GenericTrigger(
            genericVariables: [
                [key: 'WEBHOOK_TRIGGER', value: '$.trigger', defaultValue: '']
            ],
            causeString: 'Triggered by webhook',
            token: 'push_here',
            printContributedVariables: true,
            printPostContent: true
        )
    }

    options {
        skipDefaultCheckout() // Prevent automatic checkout
    }

    stages {
        stage('Start Pipeline') {
            steps {
                withChecks('Run FastAPI App') {
                    publishChecks name: 'Run FastAPI App', status: 'IN_PROGRESS', summary: 'Pipeline execution has started.'
                }
            }
        }

        stage('Clone Repository') {
            steps {
                git branch: "main", url: 'https://github.com/Swcyenh/Jenkin-MLops.git'
            }
        }

        stage('Run FastAPI Application') {
            steps {
                script {
                    try {
                        sh '''
                        #!/bin/bash

                        # Check if the container already exists
                        if docker ps -a --format '{{.Names}}' | grep -q "^api_running$"; then
                            echo "Container 'api_running' already exists. Removing it..."
                            docker stop api_running
                            docker rm -f api_running
                        fi

                        # Remove existing Docker image
                        if docker images | grep -q "api"; then
                            echo "Removing existing Docker image..."
                            docker rmi -f api
                        fi

                        # Build and run the FastAPI container
                        echo "Building the Docker image..."
                        docker build -t api .

                        echo "Running the Docker container..."
                        docker run --name api_running -p 80:80 -d api
                        '''

                        withChecks('Run FastAPI App') {
                            publishChecks name: 'Run FastAPI App', status: 'COMPLETED', conclusion: 'SUCCESS',
                                         summary: 'FastAPI container built and running successfully.'
                        }
                    } catch (e) {
                        withChecks('Run FastAPI App') {
                            publishChecks name: 'Run FastAPI App', status: 'COMPLETED', conclusion: 'FAILURE',
                                         summary: 'Pipeline failed while running the FastAPI container.'
                        }
                        throw e
                    }
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    try {
                        sh '''
                        # Run tests
                        pytest --junitxml=test-results.xml
                        '''
                        withChecks('Run Tests') {
                            publishChecks name: 'Run Tests', status: 'COMPLETED', conclusion: 'SUCCESS',
                                         summary: 'All tests passed successfully.'
                        }
                    } catch (e) {
                        withChecks('Run Tests') {
                            publishChecks name: 'Run Tests', status: 'COMPLETED', conclusion: 'FAILURE',
                                         summary: 'Some tests failed.'
                        }
                        throw e
                    }
                }
            }
        }
    }

    post {
        always {
            withChecks('Run FastAPI App') {
                publishChecks name: 'Run FastAPI App', status: 'COMPLETED', conclusion: 'NEUTRAL',
                             summary: 'Pipeline has completed execution.'
            }
        }
    }
}
