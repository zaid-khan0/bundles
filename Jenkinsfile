pipeline {
    agent any
    environment {
        // Correctly define environment variables
        DATABRICKS_HOST = 'https://adb-3576606825139482.2.azuredatabricks.net/'
        DATABRICKS_CLIENT_ID = '32da3bf3-ec3a-4d27-94b5-01ee4beeb715'
        DATABRICKS_SECRET = 'dose440e8e14fe299c9028a1cd4067fdb88a'  // Replace this with Jenkins credentials in production
        PATH='/home/linuxbrew/.linuxbrew/bin/databricks'

    }
    stages {
        stage('Checkout') {
            steps {
                // Pull the latest code from your Git repository
                git url: 'https://github.com/zaid-khan0/bundles.git', branch: 'main'
            }
        }
        stage('Deploy Notebooks to Workspace') {
            steps {
                // Directly import notebooks to the full path without looping
                sh """
                ${PATH}/databricks clusters list
                """
            }
        }
    }
}