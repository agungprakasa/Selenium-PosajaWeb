import org.jenkinsci.plugins.pipeline.modeldefinition.Utils 

//GIT CHECKOUT
def git_credentials_id = scm.userRemoteConfigs[0].credentialsId
def git_repo = scm.userRemoteConfigs[0].url
def git_branch = scm.branches[0].name
def gitCommitId
def resultlog
def pomappName = "POSAJA WEB DEV"
def urlJenkinsJob = 'http://10.24.7.14:8080/job/'
def buildNumber = currentBuild.number

def sendTelegramNotification(String message) {
    def token = "token"
    def chatId = "-4800804566"
    def url = "https://api.telegram.org/bot${token}/sendMessage"

    sh """
    curl -s -X POST ${url} -d chat_id=${chatId} -d text="${message}"
    """
}

node {
    stage('Checkout') {
        cleanWs()
        git url: "${git_repo}", branch: "${git_branch}", credentialsId: "${git_credentials_id}"
        resultlog = sh(returnStdout: true, script: 'git log  -1 --pretty=%B')
        env.M2_HOME = "/opt/maven"
        env.PATH="/opt/oc:${env.M2_HOME}/bin:${env.PATH}"
    }
    stage('Run in Docker') {
        docker.image('python:3.10-slim').inside {
            stage('Install Dependencies') {
                sh '''
                    apt-get update
                    apt-get install -y curl
                    pip install selenium
                    pip install pytz
                    pip install requests  
                '''
            }

            stage('Run Selenium Test') {
                def result

                sh 'mkdir -p output' 

                result = sh(script: 'python3 tests/login.py > output/login.log 2>&1', returnStatus: true)
                echo "login.py exit code: ${result}"

                result = sh(script: 'python3 tests/ordernoncod.py > output/ordernoncod.log 2>&1', returnStatus: true)
                echo "ordernoncod.py exit code: ${result}"

                result = sh(script: 'python3 tests/orderCOD.py > output/orderCOD.log 2>&1', returnStatus: true)
                echo "orderCOD.py exit code: ${result}"

                result = sh(script: 'python3 tests/orderCCOD.py > output/orderCCOD.log 2>&1', returnStatus: true)
                echo "orderCCOD.py exit code: ${result}"

                result = sh(script: 'python3 tests/multiorder.py > output/multiorder.log 2>&1', returnStatus: true)
                echo "multiorder.py exit code: ${result}"

                sendTelegramNotification("Reporting >> \n${env.JOB_NAME} #${env.BUILD_NUMBER}>> :")

            }
            stage('Archive Artifacts') {
                archiveArtifacts artifacts: 'output/**', fingerprint: true
            }

            stage('Send to Telegram') {
            // Kirim semua log
            sh '''
            for file in output/*.log; do
                if [ -f "$file" ]; then
                    curl -s -X POST https://api.telegram.org/bot7700320759:AAHC0ufJWzBsteFFfyoXg27cO7cCfZkcR00/sendDocument \
                        -F chat_id=-4800804566 \
                        -F document=@"$file" \
                        -F caption="Log: $(basename $file)"
                fi
            done
            '''

            // Kirim semua gambar jika ada
            sh '''
            for file in output/*.png; do
                [ -e "$file" ] || continue
                curl -s -X POST https://api.telegram.org/bot7700320759:AAHC0ufJWzBsteFFfyoXg27cO7cCfZkcR00/sendPhoto \
                    -F chat_id=-4800804566 \
                    -F photo=@"$file" \
                    -F caption="Screenshot: $(basename $file)"
            done
            '''
        }
        }
    } 
}

