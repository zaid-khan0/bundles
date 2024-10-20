node {
  def GITREPOREMOTE = "https://github.com/zaid-khan0/bundles.git"
  def GITBRANCH     = "main"
  def DATABRICKS_HOST = "https://adb-3242958281839281.1.azuredatabricks.net"
  def DEV_DIR = "/Workspace/Users/awsdatabricks00@gmail.com"
  def BUNDLETARGET  = "UAT"
  def SOURCE = "notebooks"

  stage('Checkout') {
    git branch: GITBRANCH, url: GITREPOREMOTE
  }
  stage('clusters list') {
    withCredentials([string(credentialsId: 'DATABRICKS_TOKEN', variable: 'DATABRICKS_TOKEN')]) {
      sh """#!/bin/bash
            curl -X GET "${DATABRICKS_HOST}/api/2.0/workspace/import-dir" \
            -H "Authorization: Bearer ${DATABRICKS_TOKEN}" \
            -F path = ${DEV_DIR} \
            -F content = @${SOURCE} 
         """
    }
  }
}
