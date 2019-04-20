#!/usr/bin/env groovy

pipeline {
  agent any

  stages {
    stage('Build') {
        stages('Build 1') {
            steps {
                echo 'build 1'
            }
        }
        stages('Build 2') {
            steps {
                echo 'build 2'
            }
        }
    }
    stage('NEW TEST') {
      steps {
        retry(2) {
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
