node {
    def GITREPOREMOTE = "https://github.com/zaid-khan0/bundles.git"
    def GITBRANCH     = "main"
    def DBCLIPATH     = "/home/linuxbrew/.linuxbrew/bin"
    def BUNDLETARGET  = "dev"

    stage('Checkout') {
      git branch: GITBRANCH, url: GITREPOREMOTE
    }

    stage('export dir') {
    withCredentials([string(credentialsId: 'DATABRICKS_TOKEN_DEV', variable: 'DATABRICKS_TOKEN_DEV')]) {
      sh """#!/bin/bash
            $curl -X POST "${DATABRICKS_HOST}/api/2.1/jobs/run-now" \
                -H "Authorization: Bearer ${DATABRICKS_TOKEN_DEV}" \
                -H "Content-Type: application/json" \
                -d '{
                  "job_id": 129814692029474
                }
        """
    }
  }
}
