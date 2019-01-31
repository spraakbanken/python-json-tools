workflow "Run tests" {   
    on = "push"   
    resolves = ["py35-Test"]
} 

action "py35-Build" {   
    uses = "./gh-actions/py35-pipenv"   
    args = "pipenv install --dev"
}

action "py35-Test" {
	needs = "py35-Build"
	uses = "./gh-actions/py35-pipenv"
	args = "pipenv run pytest tests"
}