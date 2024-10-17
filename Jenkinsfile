node {
  
  def DBCLIPATH = '/home/linuxbrew/.linuxbrew/bin'

  stage('List Clusters') {
    sh """#!/bin/bash
          /home/linuxbrew/.linuxbrew/bin/databricks clusters list -p newprofile
       """
  }
}
