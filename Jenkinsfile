node {

  def DBCLIPATH = '/home/linuxbrew/.linuxbrew/bin'

  stage('List Clusters') {
    withEnv([
      "DATABRICKS_HOST=https://adb-3576606825139482.2.azuredatabricks.net",
      "DATABRICKS_CLIENT_ID=32da3bf3-ec3a-4d27-94b5-01ee4beeb715",
      "DATABRICKS_SECRET=dose440e8e14fe299c9028a1cd4067fdb88a",  // Replace with actual secret or use Jenkins credentials
      "DATABRICKS_AZURE_TENANT_ID=219a8cbe-40c9-426b-bc23-ae9cd75c64bd"
    ]) {
      sh """
        export DATABRICKS_HOST=${DATABRICKS_HOST}
        export DATABRICKS_CLIENT_ID=${DATABRICKS_CLIENT_ID}
        export DATABRICKS_SECRET=${DATABRICKS_SECRET}
        export DATABRICKS_AZURE_TENANT_ID=${DATABRICKS_AZURE_TENANT_ID}
        ${DBCLIPATH}/databricks clusters list
      """
    }
  }
}
