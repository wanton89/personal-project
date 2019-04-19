pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'build'
      }
    }
    stage('Test') {
      steps {   
        sh '''
          echo hello > test.log
          cat test.log
          '''
      }
    }
  }
}
