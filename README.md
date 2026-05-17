# Reddit Top Post Explorer

A web app to display the **top post from every subreddit**, inspired by [this r/SomebodyMakeThis request](https://www.reddit.com/r/SomebodyMakeThis/comments/1awvfn/smt_a_page_that_lists_the_top_1_post_from_all/).

## Features
- Fetches the top post from 100+ popular subreddits.
- Caches results in SQLite to avoid rate limits.
- Responsive frontend with Bootstrap.
- Search/filter functionality (planned).

## Setup
1. **Install dependencies:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install flask python-dotenv
   ```

2. **Reddit API Credentials:**
   - Create a Reddit app at [https://www.reddit.com/prefs/apps](https://www.reddit.com/prefs/apps).
   - Add credentials to `.env`:
     ```ini
     REDDIT_CLIENT_ID=your_client_id
     REDDIT_CLIENT_SECRET=your_client_secret
     REDDIT_USER_AGENT=script:reddit-top-explorer:v1.0 (by /u/Femirins)
     ```

3. **Run:**
   ```bash
   python app.py
   ```
   Open [http://localhost:5000](http://localhost:5000) in your browser.

## Roadmap
- [ ] Add search/filter by subreddit.
- [ ] Deploy to Railway/GitHub Pages.
- [ ] Support more subreddits (beyond top 100).

## License
MIT