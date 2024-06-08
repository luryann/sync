### autosync 
Automatically pulls annoucements from TeamUnify and syncs it.


**How it works:**
1. Fetch News: Retrieve the latest news items from a specified source.
2. Generate HTML: Create HTML snippets for each news item that match the existing format.
3. Update HTML File: Locate the section in the HTML file where news items are to be inserted and update it.
4. Commit and Push to GitHub: Automatically push the changes to the GitHub repository.


**Step-by-Step Implementation**
1. Install Required Libraries:
   - ```pip install requests feedparser gitpython```
2. Set Up GitHub Personal Access Token:
   - Follow the GitHub documentation to create a Personal Access Token (classic) with repo permissions.
  
**Configuration**
- Replace placeholders like `your_username/your_repo`, `path/to/your/announcements.html`, `https://example.com/rss`, `your_github_token`, and `/path/to/local/repo` with your actual values.
- The `RSS_FEED_URL` should point to the RSS feed you want to fetch news from. You may replace this with an API endpoint or other data source if needed.

**Explanation of Key Parts**
- **Fetching News**: Uses the `feedparser` library to read from an RSS feed and extract the latest news items.
- **Generating HTML**: Converts news items into HTML snippets that match the current page format.
- **Updating HTML File**: Reads the current HTML content, finds the section between the markers, and replaces it with the new news content.
- **Pushing to GitHub**: Uses `GitPython` to automate adding the updated file, committing the change, and pushing it to the repository.

**Running the Script**
1. Run the script in your terminal:
```bash
python update_news.py
```

**Automating the Script**

To keep the news up-to-date automatically, you can set up a cron job or task scheduler:

```bash
# Example crontab entry to run the script every day at midnight
0 0 * * * /usr/bin/python3 /path/to/update_news.py
```
