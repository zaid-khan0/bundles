node {
  def GITREPOREMOTE = "https://github.com/zaid-khan0/bundles.git"
  def GITBRANCH     = "main"
  def DATABRICKS_HOST = "https://adb-3242958281839281.1.azuredatabricks.net"
  def DB_CLI= "/home/linuxbrew/.linuxbrew/bin"
  def DEV_DIR = "/Workspace/Users/awsdatabricks00@gmail.com"
  def BUNDLETARGET  = "UAT"
  def SOURCE = "/notebooks"

  stage('Checkout') {
    git branch: GITBRANCH, url: GITREPOREMOTE
  }
  stage('import dir') {
    withCredentials([string(credentialsId: 'DATABRICKS_TOKEN', variable: 'DATABRICKS_TOKEN')]) {
      sh """#!/bin/bash
            curl -X POST "${DATABRICKS_HOST}/api/2.1/workspace/import" \
                -H "Authorization: Bearer ${DATABRICKS_TOKEN}" \
                -H "Content-Type: application/json" \
                -d '{
                  "path": "/var/lib/jenkins/workspace/gitIntegration/notebooks",
                  "format": "SOURCE",
                  "language": "PYTHON",
                  "overwrite": true
                }'
            done
         """
    }
  }
}
