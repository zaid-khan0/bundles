node {
    def GITREPOREMOTE = "https://github.com/zaid-khan0/bundles.git"
    def DATABRICKS_HOST = "https://adb-3576606825139482.2.azuredatabricks.net"
    def GITBRANCH     = "main"
    def DBCLIPATH     = "/home/linuxbrew/.linuxbrew/bin"
    def BUNDLETARGET  = "dev"

    stage('Checkout') {
      git branch: GITBRANCH, url: GITREPOREMOTE
    }

    stage('testing') {
    withCredentials([string(credentialsId: 'DATABRICKS_TOKEN_DEV', variable: 'DATABRICKS_TOKEN_DEV')]) {
      result = sh """#!/bin/bash
            curl -X POST "${DATABRICKS_HOST}/api/2.1/jobs/run-now" \
                -H "Authorization: Bearer ${DATABRICKS_TOKEN_DEV}" \
                -d '{
                  "job_id": 129814692029474
                }' | jq '.run_id'
        """
        echo "$result"
    }
  }

}
