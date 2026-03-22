import re
from youtube_transcript_api import YouTubeTranscriptApi

def extract_video_id(url):
    patterns = [r'v=([a-zA-Z0-9_-]{11})', r'youtu\.be/([a-zA-Z0-9_-]{11})']
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    raise ValueError("Could not extract video ID from URL")

def get_transcript(url):
    video_id = extract_video_id(url)
    transcript = YouTubeTranscriptApi().fetch(video_id) if not hasattr(YouTubeTranscriptApi, 'get_transcript') else YouTubeTranscriptApi.get_transcript(video_id)
    full_text = " ".join([t.text if hasattr(t, 'text') else t["text"] for t in transcript])
    timestamped = []
    for t in transcript:
        start_val = t.start if hasattr(t, 'start') else t["start"]
        text_val = t.text if hasattr(t, 'text') else t["text"]
        mins = int(start_val) // 60
        secs = int(start_val) % 60
        timestamped.append({
            "text": text_val,
            "timestamp": f"{mins}:{secs:02d}",
            "start": start_val,
            "url": f"https://youtu.be/{video_id}?t={int(start_val)}"
        })
    return {
        "video_id": video_id,
        "full_text": full_text,
        "timestamped": timestamped,
        "word_count": len(full_text.split()),
    }
