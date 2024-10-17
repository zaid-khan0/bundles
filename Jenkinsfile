pipeline {
    agent any
    stages {
        stage('Test Jenkins Permissions') {
            steps {
                // This command should output "Hello Jenkins" if permissions are correct
                sh 'echo "Hello Jenkins"'

                // List files in the workspace to check if the user can access the directory
                sh 'ls -la /var/lib/jenkins/workspace/gitIntegration'
            }
        }
    }
}
