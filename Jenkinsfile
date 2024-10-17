node {
  def GITREPOREMOTE = "https://github.com/zaid-khan0/bundles.git"
  def GITBRANCH     = "main"
  def DBCLIPATH     = "/home/linuxbrew/.linuxbrew/bin"
  def BUNDLETARGET  = "dev"

  stage('Checkout') {
    git branch: GITBRANCH, url: GITREPOREMOTE
  }
  stage('Validate Bundle') {
    sh """#!/bin/bash
          ${DBCLIPATH}/databricks bundle validate -t ${BUNDLETARGET}
       """
  }
  stage('Deploy Bundle') {
    sh """#!/bin/bash
          ${DBCLIPATH}/databricks bundle deploy -t ${BUNDLETARGET}
       """
  }
}