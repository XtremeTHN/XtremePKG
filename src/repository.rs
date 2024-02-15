use directories::ProjectDirs;
use ureq::get;

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

        let config_dir = project_dirs.config_dir();
        let repository_dir = config_dir.join("repository.json");

        Self { repository: None }
    }
}
