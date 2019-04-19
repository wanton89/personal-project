#!/usr/bin/env groovy

pipeline {
  agent any

  stages {
    stage('Build') {
      steps {
        echo 'build'
      }
    }
    stage('NEW TEST') {
      steps {
        retry(0) {
            sh '''
            test_file="test.log"

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
      archiveArtifacts artifacts: '*log'
      cleanWs()
    }
  }
}
