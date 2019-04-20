#!/usr/bin/env groovy

pipeline {
  agent any

  stages {
    stage('Build') {
        parallel {
            stage('Build 1') {
                steps {
                    echo 'build 1'
                    for (int i = 0; i < 5; i++) {
                        build job: 'TEST_1', wait:true
                    }
                }
            }

            stage('Build 2') {
                steps {
                    echo 'build 2'
                    retry(2) {
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
                    cleanWs()
                }
            }
        }
    }
    stage('NEW TEST') {
      steps {
            retry(2) {
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
      archiveArtifacts artifacts: '*log'
      cleanWs()
    }
  }
}
