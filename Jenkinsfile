node {
  def GITREPOREMOTE = "https://github.com/zaid-khan0/bundles.git"
  def GITBRANCH     = "main"
  def DATABRICKS_HOST = "https://adb-3576606825139482.2.azuredatabricks.net/"
  def DB_CLI= "/home/linuxbrew/.linuxbrew/bin"
  def DEV_DIR = "/Workspace/Users/awsdatabricks00@gmail.com/notebooks"
  def BUNDLETARGET  = "UAT"
  def PATH = "/var/lib/jenkins/workspace/gitIntegration/myfolder"

  stage('Checkout') {
    git branch: GITBRANCH, url: GITREPOREMOTE
  }
  stage('import dir') {
    withCredentials([string(credentialsId: 'DATABRICKS_TOKEN_DEV', variable: 'DATABRICKS_TOKEN_DEV')]) {
      sh """#!/bin/bash
            curl -X GET "${DATABRICKS_HOST}/api/2.0/workspace/export" \
                -H "Authorization: Bearer ${DATABRICKS_TOKEN_DEV}" \
                -H "Content-Type: application/json" \
                -d '{
                  "path": "${DEV_DIR}",
                  "format": "DBC"
                }'
            >> result.json

            
         """
    }
  }
}
