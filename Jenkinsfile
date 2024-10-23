node {
    def GITREPOREMOTE = "https://github.com/zaid-khan0/bundles.git"
    def GITBRANCH     = "main"
    def DBCLIPATH     = "/home/linuxbrew/.linuxbrew/bin"
    def BUNDLETARGET  = "dev"

    stage('Checkout') {
      git branch: GITBRANCH, url: GITREPOREMOTE
    }

    stage('validate') {
      sh """#!/bin/bash
          ${DBCLIPATH}/databricks  bundle validate --profile DEFAULT
      """
    }

    stage('deploy'){
      sh """#!/bin/bash
          ${DBCLIPATH}/databricks  bundle deploy --profile DEFAULT
      """
    }

//    stage('Run Notebook') {
//    sh """#!/bin/bash
//        ${DBCLIPATH}/databricks bundle run -t sample_job
//    """
//  }
}
