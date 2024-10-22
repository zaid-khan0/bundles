node {
    def GITREPOREMOTE = "https://github.com/zaid-khan0/bundles.git"
    def GITBRANCH     = "main"
    def DATABRICKS_HOST_DEV = "https://adb-3576606825139482.2.azuredatabricks.net/"
    def DATABRICKS_HOST_PROD = "https://adb-3242958281839281.1.azuredatabricks.net/"
    def DEV_DIR = "/Workspace/Users/awsdatabricks00@gmail.com/notebooks"
    def LOCAL_DBC_FILE = "exported_notebooks.dbc"

    stage('git') {
        git branch: GITBRANCH, url: GITREPOREMOTE
    }

    stage('Export Notebooks') {
      withCredentials([string(credentialsId: 'DATABRICKS_TOKEN_DEV', variable: 'DATABRICKS_TOKEN_DEV')]) {
        node {
                script {
                    // Capture the output of the curl command
                    def output = sh(script: """
                       curl -X GET "https://adb-3576606825139482.2.azuredatabricks.net/api/2.0/workspace/export"\\
                             -H "Authorization: Bearer ${DATABRICKS_TOKEN_DEV}" \\
                             -d '{"path": "/Workspace/Users/awsdatabricks00@gmail.com/notebooks","format": "DBC"}' | jq '.content'
                    """, returnStdout: true).trim()
                    // Store the output in a Jenkins environment variable
                    env.DB_NOTEBOOK_CONTENT = output
                    echo "Exported notebook content stored in DB_NOTEBOOK_CONTENT environment variable, $DB_NOTEBOOK_CONTENT"
                }
            }
    }
  }

    stage('import notebooks to prod') {
        echo "idhr aaya?, $DB_NOTEBOOK_CONTENT"
        withCredentials([string(credentialsId: 'DATABRICKS_TOKEN', variable: 'DATABRICKS_TOKEN')]) {
            // Import the DBC file to the production workspace
            sh """#!/bin/bash
            curl -X POST "${DATABRICKS_HOST_PROD}/api/2.0/workspace/import" \
                -H "Authorization: Bearer ${DATABRICKS_TOKEN}" \
                -H "Content-Type: application/json" \
                -d '{
                  "path": "/Workspace",
                  "format": "DBC",
                  "content": "${DB_NOTEBOOK_CONTENT}"
                }'

            
         """
        }
    }
}
