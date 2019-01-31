workflow "Run tests" {   
    on = "push"   
    resolves = ["Test"]
} 

action "Build" {   
    uses = "./action-a"   
    args = "install-dev"
}

action "Test" {
	needs = "Build"
	uses = "./action-a"
	args = "test"
}