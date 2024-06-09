### autosync.py
High-level Python script designed to sync announcements/news from Website A ([TeamUnify](https://www.gomotionapp.com/team/cadas/page/news)) to Website B ([x](https://dareaquatics.com/news)). Designed with cron and the "set and forget" mindset in hand.

#### Notes:
- Make sure your local files are up to date.

        git pull origin main

**Dependencies**
```python
pip install requests beautifulsoup4 gitpython cloudscraper colorlog
```

**Overview**

Please note that this is a basic rundown.

1. User runs script
2. Script connects to [TeamUnify](https://www.gomotionapp.com/team/cadas/page/news) and parses all user data under div class `Item`
3. Script parses all other information required, such as date (and converts it from Unix time to readable data)
4. Script updates news.html on local machine, then pushes changes to upstream Git repository
5. DARE website is officially updated.

**Constants**
```python
GITHUB_REPO = 'https://github.com/dareaquatics/dare-website.git'          ---> Your GitHub repo; make sure to include .git duh
FILE_PATH = 'C:/Users/Ryan/Downloads/dare-website/news.html'              ---> Local path to the file you want to edit (News.html) for us
NEWS_URL = 'https://www.gomotionapp.com/team/cadas/page/news'             ---> Website that we want to clone
GITHUB_TOKEN = 'REDACTED'                                                 ---> GitHub Classic Personal Access token. Must have repo access.
LOCAL_REPO_PATH = 'C:/Users/Ryan/Downloads/dare-website'                  ---> Location to local files on your PC. Must do `git clone https://github.com/dareaquatics/dare-website.git`
```

---

### manualsync.py
Similar tool to autosync.py. However, this tool allows the user to manually add announcement entires to the website, allowing more flexibility. Uses almost the same dependencies as autosync.py
