pipeline {
    agent any
    environment {
      // Setup the environment and credentials
        JOB_NAME = 'Vinyl Island App'
        BUILD_NUMBER = '1.0.0'
        BUILD_URL = ''
        DISABLE_AUTH = 'true'
        DB_ENGINE    = 'sqlite'
    }
    stages {
            stage('Installing Packages'){
              // Steps to install venv and requirements
                steps{
                // 1. Install venv
                // 2. Create a venv directory
                // 3. Activate the venv
                // 4. Install the requirements
                    sh "python3 --version"
                    sh "wget https://bootstrap.pypa.io/get-pip.py"
                    sh "python3 get-pip.py"
                    sh "python3 -m pip install virtualenv"
                    sh "python3 -m virtualenv venv"
                    sh ". ./venv/bin/activate"
                    sh "python3 -m pip install -r requirements.txt"
                }
            }
             stage('Build'){
              // Comment Here
                steps{
                      sh 'python3 --version'
                      //sh 'newgrp docker'
                      sh 'docker run hello-world'
                      sh 'docker run --help'
                      sh 'docker-compose --version'
                      sh 'docker-compose up -d'
                      //sh 'docker-compose up -d --scale nginx=3'
                      sh 'docker-compose push'
                }
            }
            // stage('Running Unit Tests'){
              // Comment Here
               //  steps{
                   //  sh ". ./venv/bin/activate"
                    // sh "python3 -m pytest --junitxml unittests.xml"
                   //  sh "python3 -m pytest --cov-report xml:coverage.xml --cov=tests/"
                   //  sh "deactivate"
                   //  sh "rm -rf /venv"   
                   //  }
               //  }
            stage('Deploy'){
              // Comment Here
                steps{
                  echo "ready to deploy"
                }
            }
            stage('Post Build'){
              // Comment Here
                steps{
                  echo "post build actions"
                }
            }
        }
}
