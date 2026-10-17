pipeline {
    agent any
    environment {
        STUDENT_NAME    = 'Arsen'
        STUDENT_SURNAME = 'Kantpay'
        STUDENT_GROUP   = 'IT2-207'
        STUDENT_ID      = '37705'
    }
    stages {
        stage('Checkout') {
            steps {
                echo "Checking out repository from GitHub..."
            }
        }
        stage('Build') {
            steps {
                sh 'python3 -m py_compile app/app.py'
                echo "Source code compiled successfully."
            }
        }
        stage('Test') {
            steps {
                sh 'test -f app/app.py && test -f Dockerfile'
                echo "All project checks passed."
            }
        }
        stage('Docker Build') {
            steps {
                sh 'docker build -t kantpay-arsen-devops .'
            }
        }
        stage('Docker Run') {
            steps {
                sh '''
                    docker rm -f kantpay-arsen-container || true
                    docker run -d -p 8088:8088 \
                        -e STUDENT_NAME="${STUDENT_NAME}" \
                        -e STUDENT_SURNAME="${STUDENT_SURNAME}" \
                        -e STUDENT_GROUP="${STUDENT_GROUP}" \
                        -e STUDENT_ID="${STUDENT_ID}" \
                        --name kantpay-arsen-container kantpay-arsen-devops
                    sleep 2
                    docker logs kantpay-arsen-container
                    curl -s http://localhost:8088/health
                '''
                echo "Student: ${STUDENT_NAME} ${STUDENT_SURNAME}"
                echo "Group: ${STUDENT_GROUP}"
                echo "Student ID: ${STUDENT_ID}"
            }
        }
    }
}
