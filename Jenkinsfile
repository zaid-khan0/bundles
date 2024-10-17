node {

  def DBCLIPATH = '/home/linuxbrew/.linuxbrew/bin'

  stage('List Clusters') {
    withEnv([
      "DATABRICKS_HOST=https://adb-3576606825139482.2.azuredatabricks.net",
      "DATABRICKS_CLIENT_ID=32da3bf3-ec3a-4d27-94b5-01ee4beeb715",
      "DATABRICKS_SECRET=dose440e8e14fe299c9028a1cd4067fdb88a", // Store as Jenkins credentials in production
      "DATABRICKS_CLI_PATH=${DBCLIPATH}"
    ]) {
      sh """#!/bin/bash
            export DATABRICKS_HOST=${DATABRICKS_HOST}
            export DATABRICKS_CLIENT_ID=${DATABRICKS_CLIENT_ID}
            export DATABRICKS_SECRET=${DATABRICKS_SECRET}
            ${DBCLIPATH}/databricks clusters list
         """
    }
  }
}
