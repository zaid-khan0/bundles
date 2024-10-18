node {
  def GITREPOREMOTE = "https://github.com/zaid-khan0/bundles.git"
  def GITBRANCH     = "main"
  def DBCLIPATH     = "/home/linuxbrew/.linuxbrew/bin"
  def BUNDLE_ROOT = ".bundle/baby-names/development/files"
  def BUNDLETARGET  = "UAT"

  stage('Checkout') {
    git branch: GITBRANCH, url: GITREPOREMOTE
  }
  stage('deploy dir from dev to prod') {
    sh """#!/bin/bash
          ${DBCLIPATH}/databricks workspace import-dir notebooks /Workspace/Users/awsdatabricks00@gmail.com
       """
  }
}