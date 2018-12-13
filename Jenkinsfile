pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'build'
        git(url: 'git@github.com:wanton89/personal-project.git', branch: 'master')
        sh '''

firebase deploy --token "1/82yeZMaPll_x5qMgOIwt4KsopcxauASogb4zO1xcusCf8F0GFUfk7PmsRc0Cd79s"'''
      }
    }
  }
}