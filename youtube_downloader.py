from googleapiclient.discovery import build
from youtube_transcript_api import YouTubeTranscriptApi

def download_video_details(video_id, api_key):
    youtube = build('youtube', 'v3', developerKey=api_key)
    response = youtube.videos().list(
        part="snippet",
        id=video_id
    ).execute()
    description = response['items'][0]['snippet']['description']
    print("Description:\n", description)
    return description

def download_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        transcript_text = ' '.join([item['text'] for item in transcript])
        print("\nTranscript:\n", transcript_text)
        return transcript_text
    except Exception as e:
        print("An error occurred:", e)
        return None

if __name__ == "__main__":
    api_key = "YOUR_API_KEY"
    video_id = "V3DZbrIfVvg"
    description = download_video_details(video_id, api_key)
    transcript = download_transcript(video_id)
    if transcript:
        with open(f'data/transcripts/{video_id}.txt', 'w') as f:
            f.write(transcript)