pipeline {
  agent {label 'awsDeploy'}
  environment{
      DOCKERHUB_CREDENTIALS = credentials('tsanderson77-dockerhub')
      }
   stages {
     
    stage ('Build') {
      steps {
          sh 'cp ~/Dockerfile . && docker build -t tsanderson77/tasks_app:v1 . && docker scout quickview && docker scout recommendations local://tsanderson77/tasks_app:v1'
    }
}
     stage ('Login') {
        steps {
          sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
      }
}

     stage ('Push') {
        steps {
            sh 'docker push tsanderson77/tasks_app:v1 && docker image rm tsanderson77/tasks_app:v1 && docker system prune -f'
  }
     }

     stage('Init') {
       steps {
        withCredentials([string(credentialsId: 'AWS_ACCESS_KEY', variable: 'aws_access_key'), 
                        string(credentialsId: 'AWS_SECRET_KEY', variable: 'aws_secret_key')]) {
                            dir('initTerraform') {
                              sh 'terraform init' 
                            }
         }
    }
   }
      stage('Plan') {
       steps {
        withCredentials([string(credentialsId: 'AWS_ACCESS_KEY', variable: 'aws_access_key'), 
                        string(credentialsId: 'AWS_SECRET_KEY', variable: 'aws_secret_key')]) {
                            dir('initTerraform') {
                              sh 'terraform plan -out plan.tfplan -var="aws_access_key=$aws_access_key" -var="aws_secret_key=$aws_secret_key"' 
                            }
         }
    }
   }
      stage('Apply') {
       steps {
        withCredentials([string(credentialsId: 'AWS_ACCESS_KEY', variable: 'aws_access_key'), 
                        string(credentialsId: 'AWS_SECRET_KEY', variable: 'aws_secret_key')]) {
                            dir('initTerraform') {
                              sh 'terraform apply plan.tfplan' 
                            }
         }
    }
   }
 stage('Destroy') {
    steps {
          input(message: 'If you proceed to the next step it will destroy Dev?', ok: 'Continue')
          withCredentials([string(credentialsId: 'AWS_ACCESS_KEY', variable: 'aws_access_key'),
              string(credentialsId: 'AWS_SECRET_KEY', variable: 'aws_secret_key')]) {
                dir('initTerraform') {
                    sh 'terraform destroy -auto-approve -var="aws_access_key=$aws_access_key" -var="aws_secret_key=$aws_secret_key"'
                  }
            
          }
    }
}

   }
}
