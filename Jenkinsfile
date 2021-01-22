def label = "mignon-${UUID.randomUUID().toString()}"
def namespace

podTemplate(label:  label, containers: [
    containerTemplate(name: "python", image: "python:3.9.0", command: "cat", ttyEnabled: true),
    containerTemplate(name: "docker", image: "docker:19.03", command: "cat", ttyEnabled: true),
],
volumes: [
    hostPathVolume(mountPath: "/var/run/docker.sock", hostPath: "/var/run/docker.sock")
]) {
    node(label) {
        def myRepo = checkout scm
        def gitCommit = myRepo.GIT_COMMIT
        def gitBranch = myRepo.GIT_BRANCH
        def shortGitCommit = "${gitCommit[0..10]}"
        def previousGitCommit = sh(script: "git rev-parse ${gitCommit}~", returnStdout: true)

        stage("Build App"){
            container("python"){
                sh 'python --version'
                sh 'pip install -U pip setuptools'
                sh 'pip install .[dev]'
            }
        }
        stage("Test App"){
            try{
                container("python"){
                    sh "make test"
                }
            }catch(exc) {
                println "Failed to test - ${currentBuild.fullDisplayName}"
                throw(exc)
            }
        }
    }
}
