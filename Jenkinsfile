node {
  def GITREPOREMOTE = "https://github.com/zaid-khan0/bundles.git"
  def GITBRANCH     = "main"
  def DBCLIPATH     = "/home/linuxbrew/.linuxbrew/bin"
  def DATABRICKS_HOST = "https://adb-3242958281839281.1.azuredatabricks.net/"
  def BUNDLE_ROOT = ".bundle/baby-names/development/files"
  def BUNDLETARGET  = "UAT"
  def SOURCE = "notebooks"

  stage('Checkout') {
    git branch: GITBRANCH, url: GITREPOREMOTE
  }
    stage('clusters list'){
    sh """#!/bin/bash
          curl -n -X GET /api/2.0/clusters/list
       """
  }
}

















