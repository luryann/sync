## autosync.py

### Overview
This project automates the process of fetching the latest news from a specified website and updating a local GitHub repository with the fetched news items. It includes functionalities to check Git installation, clone the repository, update an HTML file with new content, and push the changes to GitHub. Additionally, unit tests are provided to ensure the reliability of the main functionalities.

#### Table of Contents
1. [Project Structure](#project-structure)
2. [Setup](#setup)
    - [Requirements](#requirements)
    - [Installation](#installation)
3. [Usage](#usage)
4. [Script Breakdown](#script-breakdown)
    - [Constants](#constants)
    - [Logging Setup](#logging-setup)
    - [Functions](#functions)
5. [Unit Tests](#unit-tests)
    - [Test Breakdown](#test-breakdown)
6. [Error Handling](#error-handling)
7. [License](#license)

### Project Structure

```
autosync/
    ├── autosync.py
    ├── manual.py
    ├── autosync_validator.py 
    └── README.md
```

### Setup

#### Requirements
- Python 3.x
- Git
- Required Python packages (listed in `requirements.txt`)

#### Installation
1. **Clone the repository**:
    ```sh
    git clone https://github.com/dareaquatics/dare-website
    cd autosync
    ```

2. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

### Usage
Run the script to start the update process:
```sh
python script.py
```

To run the unit tests:
```sh
python test_script.py
```

### Script Breakdown

### Constants
- `GITHUB_REPO`: URL of the GitHub repository.
- `NEWS_URL`: URL of the website to fetch news from.
- `GITHUB_TOKEN`: Personal Access Token for GitHub.
- `REPO_NAME`: Name of the repository to clone.
- `NEWS_HTML_FILE`: HTML file in the repository to update.

#### Logging Setup
The script uses `colorlog` for colored logging output. The logging configuration is set up to display different log levels with distinct colors.

### Functions

#### `check_git_installed()`
Checks if Git is installed on the system.
- **Returns**: `True` if Git is installed, `False` otherwise.

#### `download_portable_git()`
Downloads and extracts portable Git based on the operating system.
- **Returns**: `True` if download is successful, `False` otherwise.

#### `is_repo_up_to_date(repo_path)`
Checks if the local repository is up-to-date with the remote repository.
- **Parameters**: `repo_path` (str): Path to the local repository.
- **Returns**: `True` if the local repo is up-to-date, `False` otherwise.

#### `delete_and_reclone_repo(repo_path)`
Deletes the existing repository and clones a new one.
- **Parameters**: `repo_path` (str): Path to the local repository.

#### `clone_repository()`
Clones the repository to the current working directory and changes to the repo directory.

#### `check_github_token_validity()`
Checks if the GitHub token is valid by attempting to access the repository.

#### `fetch_news()`
Fetches the latest news from the specified website.
- **Returns**: A list of news items.

#### `convert_links_to_clickable(text)`
Converts URLs in text to clickable links.
- **Parameters**: `text` (str): Text containing URLs.
- **Returns**: Text with clickable links.

#### `generate_html(news_items)`
Generates HTML for news items.
- **Parameters**: `news_items` (list): List of news items.
- **Returns**: Generated HTML as a string.

#### `update_html_file(news_html)`
Updates the HTML file with new news items.
- **Parameters**: `news_html` (str): HTML content to update the file with.

#### `push_to_github()`
Commits and pushes the changes to GitHub.

#### `main()`
Main function to run the update process.

### Unit Tests

### Test Breakdown

#### `test_check_git_installed()`
Tests the `check_git_installed` function to ensure it detects Git installation.

#### `test_check_git_not_installed()`
Tests the `check_git_installed` function to ensure it correctly identifies when Git is not installed.

#### `test_download_portable_git()`
Tests the `download_portable_git` function to ensure it downloads Git correctly.

#### `test_is_repo_up_to_date()`
Tests the `is_repo_up_to_date` function to check if the repository is up-to-date.

#### `test_delete_and_reclone_repo()`
Tests the `delete_and_reclone_repo` function to ensure it deletes and reclones the repository.

#### `test_clone_repository()`
Tests the `clone_repository` function to ensure it clones the repository correctly.

#### `test_check_github_token_validity()`
Tests the `check_github_token_validity` function to validate the GitHub token.

#### `test_fetch_news()`
Tests the `fetch_news` function to ensure it fetches news correctly.

#### `test_convert_links_to_clickable()`
Tests the `convert_links_to_clickable` function to ensure URLs are converted to clickable links.

#### `test_generate_html()`
Tests the `generate_html` function to ensure HTML is generated correctly for news items.

#### `test_update_html_file()`
Tests the `update_html_file` function to ensure the HTML file is updated correctly.

### Error Handling
The script includes robust error handling for common issues such as:
- Invalid GitHub token.
- Git not installed.
- Errors during Git operations.
- File access issues.
- Network request failures.

If an error occurs, a descriptive error message is logged, and the script terminates gracefully without marking the process as completed.

