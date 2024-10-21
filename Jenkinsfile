node {
  def DATABRICKS_HOST = "https://adb-3242958281839281.1.azuredatabricks.net"
  def DB_CLI= "/home/linuxbrew/.linuxbrew/bin"

  stage('import dir') {
      sh """#!/bin/bash
            export DATABRICKS_HOST=${DATABRICKS_HOST}
            ${DB_CLI}/databricks/clusters/list           
         """
  }
}
