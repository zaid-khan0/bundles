pipeline {
    agent any
    environment {
        // Correctly define environment variables
        DATABRICKS_HOST = 'https://adb-3576606825139482.2.azuredatabricks.net/'
        DATABRICKS_CLIENT_ID = 'f9518eb9c4894d8387914ec4a015e25f5a99dc731f760df8bff1f130183f225a'
        DATABRICKS_SECRET = 'dose16691054ba5ed40df5dbe4a09f14a54a'  // Replace this with Jenkins credentials in production
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
                #!/bin/bash
                ${PATH}databricks workspace import_dir \
                /notebooks/ /Workspace/Users/awsdatabricks00@gmail.com/jenkinsAG \
                """
            }
        }
    }
}
