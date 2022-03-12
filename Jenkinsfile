pipeline {
    agent any
    environment {
      // Setup the environment and credentials
        JOB_NAME = 'Vinyl Island App'
        BUILD_NUMBER = '1.0.0'
        BUILD_URL = ''
        DISABLE_AUTH = 'true'
        DB_ENGINE    = 'sqlite'
	SECRET_KEY = credentials('sshKeyVIserver')
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
                      sh 'docker-compose --version'
                      sh 'docker-compose up -d'
                      //sh 'docker-compose up -d --scale nginx=3'
                }
            }
            stage('Push'){
                steps{
		withCredentials([string(credentialsId: 'c4c29728-20ac-4c4d-a67b-3f7cccc8c424', variable: 'dockerHubPWD')]) {
              // Comment Here
		      sh 'docker login -u iancollinge -p JKbas18ja'
		      sh 'docker-compose push'
		}
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
                  // some block
                      sh 'scp docker-compose.yaml ian@10.0.0.21'
                      sh 'ssh ian@10.0.0.21 docker deploy --compose-file docker-compose.yaml app'
                }
            }
		    
            stage('Post Build Actions') {
		// One or more steps need to be included within the steps block.
  		steps {
		     sh 'echo build completed'
  		}
		  post {
    		  always {
			  sh 'docker logout'
      		  // One or more steps need to be included within each condition's block.
    		}
  	      }
            }
       }
    }
