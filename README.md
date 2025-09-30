# Baseer Ali Twitter Bot 👑🔥

Automated Twitter bot for **#BaseerAli Army** – Bigg Boss 19 edition.

## 🚀 Features
- Tweets every 5 minutes using GitHub Actions
- Mix cycle: 2 hype tweets → 1 roast tweet
- Auto adds random hashtags + emojis
- Picks matching image (king / friends / clown / zoo gang)
- Logs every tweet with timestamp in `tweet_log.txt`

## 📂 Repo Structure
- `tweet_bot.py` → Main bot logic
- `hype.txt` → Baseer hype tweets
- `burai.txt` → Roast tweets
- `images/` → Store Baseer Ali photos
- `.github/workflows/tweet.yml` → Automation workflow
- `state.txt` → Tracks tweet index
- `tweet_log.txt` → Tweet history

## 🛠 Setup
1. Fork this repo
2. Go to **Settings → Secrets and variables → Actions**
3. Add secrets:
   - `API_KEY`
   - `API_SECRET`
   - `ACCESS_TOKEN`
   - `ACCESS_SECRET`
4. Upload Baseer photos into `images/`
5. GitHub Actions will auto-tweet every 5 mins ✅

## 🗂 Project Board
Recommended Columns:
- **To Do** → Add retweet support, email log, multi-account
- **In Progress** → Upload images, new hype tweets
- **Done** → Auto tweets, hashtags, emojis, logs
