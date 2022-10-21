pipeline {
	agent {
		docker {
			image 'python:3.8'
		}
	}
	environment {
		HOME = "${env.WORKSPACE}@tmp"
		BIN_PATH = "${HOME}/.local/bin/"
	}
	stages {
		stage('Git Clone') {
			steps {
				git changelog: false, url: 'http://gitlab.devops.ru/vika_cat/vika_cat.git'
			}
		}
		stage('Prepare') {
			steps {
				/* аналогично подготовительному этапу во 3 л.р.*/
				sh 'python --version'
				sh 'pip install virtualenv'
				sh "${BIN_PATH}virtualenv venv"
				sh 'bash -c "source venv/bin/activate"'
				sh 'pip install -r requirements.txt'
			}
		}
		stage('Test') {
			steps{
				/* меняем запуск теста, который был в 3 л.р.*/
				sh 'nohup python src/main.py &'
				sh '${BIN_PATH}pytest -v tests/tests.py'
				sh "${BIN_PATH}flake8 ."
				sh "${BIN_PATH}mypy ."
			}
		}
	}
}