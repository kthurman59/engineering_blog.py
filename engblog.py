import requests
import feedparser

# List of engineering blog URLs
engineering_blogs = {
    "Netflix Techblog": "https://medium.com/feed/netflix-techblog",
    "Uber Blog": "https://eng.uber.com/feed/",
    "Cloudflare Blog": "https://blog.cloudflare.com/rss/",
    "Engineering at Meta": "https://engineering.fb.com/feed/",
    "Linkedin Engineering": "https://engineering.linkedin.com/blog.rss",
    "Discord Blog": "https://blog.discord.com/feed",
    "AWS Architecture": "https://aws.amazon.com/architecture/blog/feed/",
    "Slack Engineering": "https://slack.engineering/feed/",
    "Stripe Blog": "https://stripe.com/blog/rss",
}


# Function to fetch and display new posts
def fetch_new_posts():
    for blog_name, blog_url in engineering_blogs.items():
        print(f"Checking {blog_name}...")
        feed = feedparser.parse(blog_url)
        if len(feed.entries) > 0:
            latest_post = feed.entries[0]
            print(f"Latest post from {blog_name}:")
            print(f"Title: {latest_post.title}")
            print(f"Link: {latest_post.link}")
            print()
        else:
            print(f"No new posts on {blog_name}")
        print("-----------------------------")


if __name__ == "__main__":
    fetch_new_posts()
