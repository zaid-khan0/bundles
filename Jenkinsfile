node {
    def DBCLIPATH = '/home/linuxbrew/.linuxbrew/bin'
  
  stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/zaid-khan0/bundles.git', branch: 'main'
            }
        }
        stage('Deploy Notebooks to Workspace') {
            steps {
                sh '''
                #!/bin/bash
                ${DBCLIPATH}/databricks workspace import-dir notebooks /Workspace/Users/awsdatabricks00@gmail.com/jenkinsAG
                '''
            }
        }
  }}