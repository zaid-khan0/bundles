node {
    def GITREPOREMOTE = "https://github.com/zaid-khan0/bundles.git"
    def DATABRICKS_HOST = "https://adb-3576606825139482.2.azuredatabricks.net"
    def GITBRANCH     = "main"
    def DBCLIPATH     = "/home/linuxbrew/.linuxbrew/bin"
    def BUNDLETARGET  = "dev"
    def result = ""
    def status = ""
    def dir = ""
    def DEV_DIR = "/Workspace/Users/awsdatabricks00@gmail.com/ETL_Testing/test/"

    stage('Checkout') {
        git branch: GITBRANCH, url: GITREPOREMOTE
    }

    stage('Testing') {
        withCredentials([string(credentialsId: 'DATABRICKS_TOKEN_DEV', variable: 'DATABRICKS_TOKEN_DEV')]) {
            result = sh(script: """#!/bin/bash
                curl -X POST "${DATABRICKS_HOST}/api/2.1/jobs/run-now" \
                    -H "Authorization: Bearer ${DATABRICKS_TOKEN_DEV}" \
                    -d '{
                      "job_id": 129814692029474
                    }' | jq '.run_id'
            """, returnStdout: true).trim()
            
            echo "Run ID: ${result}"
        }
    }

    stage('Please let me Sleep 2 minutes more') {
        sleep(time: 2, unit: "MINUTES")
    }

    stage('Check Status') {
        echo "Run ID: ${result}"
        withCredentials([string(credentialsId: 'DATABRICKS_TOKEN_DEV', variable: 'DATABRICKS_TOKEN_DEV')]) {
            status = sh(script: """#!/bin/bash
                curl -X GET "${DATABRICKS_HOST}/api/2.1/jobs/runs/get" \
                    -H "Authorization: Bearer ${DATABRICKS_TOKEN_DEV}" \
                    -d '{
                      "run_id": ${result}
                    }' | jq -r '.status.termination_details.type'
            """, returnStdout: true).trim()
            echo "Job Status: ${status}"
        }
    }

    stage('Import') {
        script {
            if (status == "SUCCESS") {
                echo "Job completed successfully, proceeding with import."

                // Export the workspace content
                withCredentials([string(credentialsId: 'DATABRICKS_TOKEN_DEV', variable: 'DATABRICKS_TOKEN_DEV')]) {
                    dir = sh(script: """#!/bin/bash
                        curl -X GET "${DATABRICKS_HOST}/api/2.0/workspace/export" \
                            -H "Authorization: Bearer ${DATABRICKS_TOKEN_DEV}" \
                            -H "Content-Type: application/json" \
                            -d '{
                              "path": "${DEV_DIR}",
                              "format": "SOURCE"
                            }' | jq -r '.content'
                    """, returnStdout: true).trim()
                    echo "Exported content: ${dir}"
                }

                // Import the workspace content
                withCredentials([string(credentialsId: 'DATABRICKS_TOKEN_DEV', variable: 'DATABRICKS_TOKEN_DEV')]) {
                    sh(script: """#!/bin/bash
                        curl -X POST "${DATABRICKS_HOST}/api/2.0/workspace/import" \
                            -H "Authorization: Bearer ${DATABRICKS_TOKEN_DEV}" \
                            -H "Content-Type: application/json" \
                            -d '{
                              "path": "/Workspace/Users/awsdatabricks00@gmail.com/gggg",
                              "format": "SOURCE",
                              "content": "${dir}",
                              "overwrite": true
                            }'
                    """)
                }
            } else {
                error "Job did not complete successfully; current status: ${status}"
            }
        }
    }
}
