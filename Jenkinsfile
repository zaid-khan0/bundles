node {
  def GITREPOREMOTE = "https://github.com/zaid-khan0/bundles.git"
  def GITBRANCH     = "main"
  def DATABRICKS_HOST = "https://adb-3242958281839281.1.azuredatabricks.net"
  def DB_CLI= "/home/linuxbrew/.linuxbrew/bin"
  def DEV_DIR = "/Workspace/Users/awsdatabricks00@gmail.com/new/"
  def BUNDLETARGET  = "UAT"
  def PATH = "/var/lib/jenkins/workspace/gitIntegration/myfolder"

  stage('Checkout') {
    git branch: GITBRANCH, url: GITREPOREMOTE
  }
  stage('import dir') {
      sh """#!/bin/bash
            export DATABRICKS_HOST=${DATABRICKS_HOST}
            ${DB_CLI}/databricks/clusters/list           
         """
  }
}
