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

    stage('export notebooks from dev') {
        withCredentials([string(credentialsId: 'DATABRICKS_TOKEN_DEV', variable: 'DATABRICKS_TOKEN_DEV')]) {
            script {
                // Export the notebooks and save to a local DBC file
                sh """
                curl -s -X GET "${DATABRICKS_HOST_DEV}/api/2.0/workspace/export" \
                    -H "Authorization: Bearer ${DATABRICKS_TOKEN_DEV}" \
                    -H "Content-Type: application/json" \
                    -d '{
                        "path": "${DEV_DIR}",
                        "format": "DBC"
                    }' -o ${LOCAL_DBC_FILE}
                """
                
                // Check if the file was exported successfully
                sh "ls -l ${LOCAL_DBC_FILE}"
            }
        }
    }

    stage('import notebooks to prod') {
        withCredentials([string(credentialsId: 'DATABRICKS_TOKEN', variable: 'DATABRICKS_TOKEN')]) {
            // Import the DBC file to the production workspace
            sh """
            curl -s -X POST "${DATABRICKS_HOST_PROD}/api/2.0/workspace/import" \
                -H "Authorization: Bearer ${DATABRICKS_TOKEN}" \
                -F "path=${DEV_DIR}" \
                -F "format=DBC" \
                -F "file=@${LOCAL_DBC_FILE}" \
                -F "overwrite=true"
            """
        }
    }
}
