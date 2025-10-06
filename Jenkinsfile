pipeline {
    agent any

    environment {
        VENV = "venv"
    }

    stages {

        stage('Clone Repository') {
            steps {
                git branch: 'main', 
                    url: 'https://github.com/rajashribhamare/Django-Employee-Management.git', 
                    credentialsId: 'github-pat'
            }
        }

        stage('Set up Python Environment') {
            steps {
                bat '''
                python -m venv %VENV%
                call %VENV%\\Scripts\\activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Django Tests') {
            steps {
                bat '''
                call %VENV%\\Scripts\\activate
                python manage.py test
                '''
            }
        }

        stage('Build Complete') {
            steps {
                echo '✅ Django project build successful!'
            }
        }

        stage('Deploy (Optional)') {
            steps {
                bat '''
                call %VENV%\\Scripts\\activate
                python manage.py migrate
                python manage.py collectstatic --noinput
                '''
                echo '🚀 Django project deployed successfully!'
            }
        }

    }

    post {
        success {
            echo '🎉 Pipeline executed successfully!'
        }
        failure {
            echo '❌ Pipeline failed!'
        }
    }
}


