properties([githubProjectProperty(displayName: '', projectUrlStr: 'https://github.com/shay79il/Trigo-appA/'), parameters([[$class: 'ChoiceParameter', choiceType: 'PT_SINGLE_SELECT', filterLength: 1, filterable: false, name: 'ENV_NAME', randomName: 'choice-parameter-322005257306874', script: [$class: 'GroovyScript', fallbackScript: [classpath: [], sandbox: false, script: 'return [\'DEV\']'], script: [classpath: [], sandbox: false, script: 'return [\'DEV\',\'PRODUCTION\']']]], [$class: 'CascadeChoiceParameter', choiceType: 'PT_SINGLE_SELECT', filterLength: 1, filterable: false, name: 'REGION', randomName: 'choice-parameter-322005293393729', referencedParameters: 'ENV_NAME', script: [$class: 'GroovyScript', fallbackScript: [classpath: [], sandbox: false, script: 'return [\'us-east-1\']'], script: [classpath: [], sandbox: false, script: '''def choices
switch(ENV_NAME){
    case \'PRODUCTION\':
        choices = [\'us-east-1\', \'us-east-2\', \'us-east-3\']
        break
    case \'DEV\':
        choices = [\'us-west-1\', \'us-west-2\']
        break
    default:
        choices = [\'us-east-1\']
        break
}
return choices''']]]]), [$class: 'JobLocalConfiguration', changeReasonComment: ''], pipelineTriggers([githubPush()])])
pipeline {
    agent any

    stages {
        stage ('(1) Git clone') {
            steps {
                git branch: 'main', url: 'https://github.com/shay79il/Trigo-appA'
            }
        }
        stage ('(2) Build image') {
            steps {
                sh 'docker build -t shay79il/app-a .'
            }
        }
    }

    post {
        success {
            echo "${env.BUILD_URL}"
            echo "======= SUCCESS =======\n======= SUCCESS =======\n======= SUCCESS =======\n"

            // stage ('(1) Push image to dockerHub')
            sh 'docker push shay79il/app-a'

            // sudo cp .kube/config ~jenkins/.kube/config
            // sudo chown jenkins: ~jenkins/.kube/config
            // stage ('(2) Add Helm Chart repo')
            sh 'helm repo add myhelmrepo https://shay79il.github.io/helm-chart/'

            // stage ('(3) Update Helm Chart repo')
            sh 'helm repo update myhelmrepo'

            // stage ('(4) Deploy Helm Chart App_A')
            sh 'helm upgrade --install app-a myhelmrepo/trigo-app-a  \
                --set app.region=${REGION} \
                --set app.env=${ENV_NAME} \
                --set app.replicas=${REPLICAS}'

        }
        failure {
            echo "${env.BUILD_URL}"
            echo "======= FAIL !!! =======\n======= FAIL !!! =======\n======= FAIL !!! =======\n"
            echo "======= Build docker image \nshay79il/appa FAILED!!! =======\n"
        }
    }
}