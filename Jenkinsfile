node {
  def DB_CLI= "/home/linuxbrew/.linuxbrew/bin"
  def DEV_DIR = "/Workspace/Users/awsdatabricks00@gmail.com/notebooks"

  stage('import dir') {
      sh """#!/bin/bash
            ${DB_CLI}/databricks clusters list        
         """
    }
  }

node {
  def GITREPOREMOTE = "https://github.com/zaid-khan0/bundles.git"
  def GITBRANCH     = "main"
  def DATABRICKS_HOST_DEV = "https://adb-3576606825139482.2.azuredatabricks.net/"
  def DATABRICKS_HOST_PROD = "https://adb-3242958281839281.1.azuredatabricks.net/"
  def DB_CLI= "/home/linuxbrew/.linuxbrew/bin"
  def DEV_DIR = "/Workspace/Users/awsdatabricks00@gmail.com/notebooks"
  def BUNDLETARGET  = "UAT"
  def PATH = "/var/lib/jenkins/workspace/gitIntegration"

  stage('git') {
    git branch: GITBRANCH, url: GITREPOREMOTE
  }
  stage('export notebooks from dev') {
    withCredentials([string(credentialsId: 'DATABRICKS_TOKEN_DEV', variable: 'DATABRICKS_TOKEN_DEV')]) {
      sh """#!/bin/bash
            result=$(curl -X GET "${DATABRICKS_HOST_DEV}/api/2.0/workspace/export" \
                -H "Authorization: Bearer ${DATABRICKS_TOKEN_DEV}" \
                -H "Content-Type: application/json" \
                -d '{
                  "path": "${DEV_DIR}",
                  "format": "DBC"
                }'| jq '.content')          
         """
    }
  }
  stage('import notebooks to prod') {
    withCredentials([string(credentialsId: 'DATABRICKS_TOKEN', variable: 'DATABRICKS_TOKEN')]) {
      sh """#!/bin/bash
            $curl -X GET "${DATABRICKS_HOST_PROD}/api/2.0/workspace/import" \
                -H "Authorization: Bearer ${DATABRICKS_TOKEN}" \
                -H "Content-Type: application/json" \
                -d '{
                  "path": "${DEV_DIR}",
                  "format": "DBC"
                  "content": "${result}"
                }
                     
         """
    }
  }
}
