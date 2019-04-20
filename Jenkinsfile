pipeline {
  agent any
  stages {
    stage('Build') {
      parallel {
        stage('Build 1') {
          steps {
            echo 'build 1'
          }
        }
        stage('Build 2') {
          steps {
            echo 'build 2'
            retry(count: 2) {
              sh '''
                        test_file="asd.log"

                        if [ -f $test_file ]; then
                            exit 0
                        else
                            touch $test_file
                            echo "create ${test_file}"
                            exit 1
                        fi
                            '''
            }

          }
        }
      }
    }
    stage('NEW TEST') {
      steps {
        retry(count: 2) {
          sh '''
                test_file="asd.log"

                if [ -f $test_file ]; then
                    exit 0
                else
                    touch $test_file
                    echo "create ${test_file}"
                    exit 1
                fi
                '''
        }

      }
    }
    stage('Another test') {
      steps {
        echo 'PASS!'
      }
    }
  }
  post {
    always {
      archiveArtifacts '*log'
      cleanWs()

    }

  }
}