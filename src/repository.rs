use directories::ProjectDirs;

use std::fs::{create_dir_all, File};
use std::io::{Read, Write};

struct Package {
    name: String,
    description: String,
    url: String,
}

pub struct Repository {
    repository: Option<Vec<Package>>,
}

impl Repository {
    pub fn new() -> Self {
        let project_dirs = ProjectDirs::from("com", "github", "XtremePKG").unwrap();
        println!("Config dir: {:?}", project_dirs.config_dir());
        create_dir_all(project_dirs.config_dir()).unwrap();

        let config_dir = project_dirs.config_dir();
        let repository_dir = config_dir.join("repository.json");

        if !repository_dir.exists() {
            let content = ureq::get("https://api.github.com/users/XtremeTHN/repos").call().expect(
                "Failed to retrieve repository list from GitHub. Is the internet connection working?",
            );

            let mut repo_file = File::create(repository_dir).unwrap();
            repo_file.write_all(content.into_string().unwrap().as_bytes());
        }

        Self { repository: None }
    }
}
