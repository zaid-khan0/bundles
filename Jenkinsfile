node {
  def DB_CLI= "/home/linuxbrew/.linuxbrew/bin"
  def DEV_DIR = "/Workspace/Users/awsdatabricks00@gmail.com/notebooks"

  stage('import dir') {
      sh """#!/bin/bash
            ${DB_CLI}/databricks clusters list        
         """
    }
  }

