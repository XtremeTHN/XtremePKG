use directories::ProjectDirs;
use std::path::PathBuf;
use std::fs::File;
use std::io::Write;

struct Repo {
    name: String,
    description: String,
    url: String
}

struct Repository {
    root: PathBuf,
    repos: Vec<Repo>
}

impl Repository {
    pub fn new() -> Repository {
        
    }

    pub fn sync_repo() -> () {
        let root = ProjectDirs::from("", "", "xtremepkg").unwrap();
        let req_url: &str = "https://api.github.com/users/XtremeTHN/repos";
        let request = ureq::get(req_url);

        let config_dir = root.config_dir().to_path_buf();
        let repo_path = config_dir.join("repository.json");
        
        let repo_content = request
            .call().unwrap()
            .into_string().unwrap()

        if !repo_path.exists() {
            let mut repo_file = File::create(repo_path).unwrap();
            repo_file.write_all(repo_content.as_bytes());
            
    
        }

        

    }
}
