properties([pipelineTriggers([pollSCM('* * * * *')])])
node {
    stage("clone"){
        git "https://github.com/Ariel7871/DevOps3006.git"
    }
    stage("show files"){
        sh "ls -l"
    }
}
