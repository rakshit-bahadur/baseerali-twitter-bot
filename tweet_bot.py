import tweepy
import os
import random
from dotenv import load_dotenv
from datetime import datetime

# Load API keys
load_dotenv()
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("ACCESS_SECRET")

# Auth
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# Files
hype_file = "hype.txt"
burai_file = "burai.txt"
state_file = "state.txt"
log_file = "tweet_log.txt"
image_folder = "images"

# Load tweets
with open(hype_file, "r", encoding="utf-8") as f:
    hype_tweets = [line.strip() for line in f if line.strip()]
with open(burai_file, "r", encoding="utf-8") as f:
    burai_tweets = [line.strip() for line in f if line.strip()]

# Track index
if os.path.exists(state_file):
    with open(state_file, "r") as f:
        index = int(f.read().strip())
else:
    index = 0

# Tweet selection: 2 hype → 1 burai
cycle = index % 3
if cycle in (0, 1):  # hype tweet
    tweet = hype_tweets[(index // 3 * 2 + cycle) % len(hype_tweets)]
    tweet_type = "hype"
else:  # burai tweet
    tweet = burai_tweets[(index // 3) % len(burai_tweets)]
    tweet_type = "burai"

# --- Hashtag Pools ---
hype_hashtags = [
    "#BaseerAli", "#BaseerAli", "#BaseerAli",
    "#BiggBoss19", "#BaseerAliArmy", "#BaseerAliForTheWin",
    "#TeamBaseer", "#VoteForBaseerAli", "#BB19"
]

roast_hashtags = [
    "#Bailbuddhi", "#Zazu", "#VictimCard", "#RonaDhona", "#HoteRahoBully",
    "#CircusGang", "#FootageKhaaoGang", "#RonaMachine",
    "#FakeFriendship", "#LoserGang", "#CryBabyClub", "#GroupismKaBaap"
]

# --- Emoji Pool ---
emojis = ["🔥", "💯", "👑", "🦁", "😂", "🤡", "😎", "💪", "❤️", "📉", "📈"]

# Hashtag selection logic
if tweet_type == "hype":
    chosen_tags = random.choices(hype_hashtags, k=random.randint(3, 6))
    # 30% chance add 1 roast hashtag for spice
    if random.random() < 0.3:
        chosen_tags.append(random.choice(roast_hashtags))
else:  # burai tweet
    chosen_tags = random.choices(roast_hashtags + hype_hashtags, k=random.randint(5, 8))

extra_tags = " ".join(chosen_tags)
extra_emojis = "".join(random.choices(emojis, k=random.randint(2, 4)))
final_tweet = f"{tweet} {extra_tags} {extra_emojis}"

# --- Match Image Category ---
category = ""
if "clown" in tweet.lower() or "rona" in tweet.lower():
    category = "clown"
elif "king" in tweet.lower() or "👑" in tweet or "🦁" in tweet:
    category = "baseer_king"
elif "friends" in tweet.lower() or "doston" in tweet.lower():
    category = "baseer_friends"
elif "zoo" in tweet.lower() or "circus" in tweet.lower():
    category = "zoo_gang"

image_files = []
if category:
    image_files = [f for f in os.listdir(image_folder) if category in f.lower()]

# Post + log
image_used = "None"
status_message = ""

try:
    if image_files:
        image_path = os.path.join(image_folder, random.choice(image_files))
        api.update_status_with_media(status=final_tweet, filename=image_path)
        image_used = os.path.basename(image_path)
        status_message = "✅ Tweet with photo posted"
    else:
        api.update_status(final_tweet)
        status_message = "✅ Tweet posted"
except Exception as e:
    status_message = f"⚠️ Error posting tweet: {e}"

with open(state_file, "w") as f:
    f.write(str(index + 1))

with open(log_file, "a", encoding="utf-8") as log:
    log.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {status_message}\n")
    log.write(f"Tweet: {final_tweet}\n")
    log.write(f"Image: {image_used}\n\n")

print(status_message, "| Tweet:", final_tweet, "| Image:", image_used)
