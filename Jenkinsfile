node {
  
  // Define the actual Databricks CLI installation path
  def DBCLIPATH = '/home/linuxbrew/.linuxbrew/bin'  // Update with actual path

  stage('List Clusters') {
    sh """#!/bin/bash
          ${DBCLIPATH}/databricks clusters list -p newprofile
       """
  }
}
