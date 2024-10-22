node {
    def GITREPOREMOTE = "https://github.com/zaid-khan0/bundles.git"
    def GITBRANCH     = "main"
    def DATABRICKS_HOST_DEV = "https://adb-3576606825139482.2.azuredatabricks.net/"
    def DATABRICKS_HOST_PROD = "https://adb-3242958281839281.1.azuredatabricks.net/"
    def DEV_DIR = "/Workspace/Users/awsdatabricks00@gmail.com/notebooks"
    def BUNDLETARGET  = "UAT"
    def PATH = "/var/lib/jenkins/workspace/gitIntegration"

    stage('git') {
        git branch: GITBRANCH, url: GITREPOREMOTE
    }
    
    stage('export notebooks from dev') {
        withCredentials([string(credentialsId: 'DATABRICKS_TOKEN_DEV', variable: 'DATABRICKS_TOKEN_DEV')]) {
            script {
                response = sh(
                    script: """#!/bin/bash
                    curl -s -X GET "${DATABRICKS_HOST_DEV}/api/2.0/workspace/export" \
                        -H "Authorization: Bearer ${DATABRICKS_TOKEN_DEV}" \
                        -H "Content-Type: application/json" \
                        -d '{
                            "path": "${DEV_DIR}",
                            "format": "DBC"
                        }' | jq -r '.content'
                    """,
                    returnStdout: true
                ).trim()
                env.EXPORTED_CONTENT = response
                echo "$EXPORTED_CONTENT"
            }
        }
    }
    
    stage('import notebooks to prod') {
        echo "$EXPORTED_CONTENT"
        withCredentials([string(credentialsId: 'DATABRICKS_TOKEN', variable: 'DATABRICKS_TOKEN')]) {
            sh """#!/bin/bash
            curl -s -X POST "${DATABRICKS_HOST_PROD}/api/2.0/workspace/import" \
                -H "Authorization: Bearer ${DATABRICKS_TOKEN}" \
                -H "Content-Type: application/json" \
                -d '{
                    "path": "${DEV_DIR}",
                    "format": "DBC",
                    "content": "${EXPORTED_CONTENT}",
                    "overwrite": true
                }'
            """
        }
    }
}
