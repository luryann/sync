# Does not work currently, just removes pre-existing news made by manualsync.py

import os
import requests
import feedparser
from datetime import datetime
from git import Repo

# Constants
GITHUB_REPO = 'dareaquatics/dare-website'
FILE_PATH = 'C:/Users/Ryan/Downloads/dare-website/news.html'
RSS_FEED_URL = 'https://www.gomotionapp.com/team/cadas/page/news'
GITHUB_TOKEN = 'REDACTED' 
LOCAL_REPO_PATH = 'C:/Users/Ryan/Downloads/dare-website'

# Fetch the latest news from an RSS feed
def fetch_news():
    news_feed = feedparser.parse(RSS_FEED_URL)
    news_items = []

    for entry in news_feed.entries[:5]:  # Fetch top 5 news items
        news_items.append({
            'title': entry.title,
            'link': entry.link,
            'date': entry.published,
            'summary': entry.summary
        })
    
    return news_items

# Generate HTML for news items
def generate_html(news_items):
    news_html = ''

    for item in news_items:
        date_obj = datetime.strptime(item['date'], '%a, %d %b %Y %H:%M:%S %Z')
        formatted_date = date_obj.strftime('%B %d, %Y')

        news_html += f'''
        <div class="news-item">
            <h2 class="news-title">{item["title"]}</h2>
            <p class="news-date">Published on {formatted_date}</p>
            <p class="news-content">{item["summary"]}</p>
            <p><a href="{item["link"]}">Read more</a></p>
        </div>
        '''

    return news_html

# Update the HTML file with new news items
def update_html_file(news_html):
    with open(FILE_PATH, 'r', encoding='utf-8') as file:
        content = file.read()

    # Define markers for the section to be replaced
    start_marker = '<!-- START UNDER HERE -->'
    end_marker = '<!-- Add more news items here -->'
    start_index = content.find(start_marker) + len(start_marker)
    end_index = content.find(end_marker)

    # Update the content between markers
    updated_content = content[:start_index] + '\n' + news_html + '\n' + content[end_index:]

    with open(FILE_PATH, 'w', encoding='utf-8') as file:
        file.write(updated_content)


# Commit and push the changes to GitHub
def push_to_github():
    repo = Repo(LOCAL_REPO_PATH)
    repo.git.add(FILE_PATH)
    repo.index.commit('automated:: update news.html')
    origin = repo.remote(name='origin')
    origin.push()

# Main function to run the update process
def main():
    print("Fetching latest news...")
    news_items = fetch_news()

    print("Generating HTML...")
    news_html = generate_html(news_items)

    print("Updating HTML file...")
    update_html_file(news_html)

    print("Pushing changes to GitHub...")
    push_to_github()

    print("Done!")

if __name__ == "__main__":
    main()
