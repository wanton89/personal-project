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
        retry(2) {
            sh '''
                #!/bin/sh
                echo hello > new.log
                cat test.log
                if [ $? -ne 0 ]; then
                  echo retry > test.log
                  exit 1;
                fi
                '''
          }
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
