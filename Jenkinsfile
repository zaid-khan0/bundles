node {
  
  def DBCLIPATH = '/home/linuxbrew/.linuxbrew/bin'

  stage('List Clusters') {
    sh """#!/bin/bash
          ${DBCLIPATH}/databricks clusters list
       """
  }
}
