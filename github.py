class GitHubRepo:
    def __init__(self, name, language, num_stars):
        self.name = name
        self.language = language
        self.num_stars = num_stars

    def __str__(self):
        return f"->{self.name} is a {self.language} repo with {self.num_stars} stars."
    

vue = GitHubRepo("Vue", "JavaScript", 50000)

print(vue)