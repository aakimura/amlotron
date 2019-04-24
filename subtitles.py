from youtube_transcript_api import YouTubeTranscriptApi

video_id = 'WBc7gNgPw4k'
subtitles = YouTubeTranscriptApi.get_transcript(video_id)

transcript = []

for sentence in subtitles:
    text = sentence['text']
    transcript.append(text)

transcript = (' ').join(transcript)
