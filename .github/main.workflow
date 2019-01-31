workflow "Run tests" {   
    on = "push"   
    resolves = ["Test"]
} 

action "Build" {   
    uses = "./action-a"   
    args = "pipenv install --dev"
}

action "Test" {
	needs = "Build"
	uses = "./action-a"
	args = "pipenv run pytest tests"
}