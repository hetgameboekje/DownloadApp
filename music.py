import re
from pytube import Playlist, exceptions
from pydub import AudioSegment
import os

def download_playlist(playlist_url, download_dir):
    YOUTUBE_STREAM_AUDIO = '140'  # Modify the value to download a different stream

    # Create a Playlist object
    playlist = Playlist(playlist_url)

    # This fixes the empty playlist.videos list
    playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
    count = 0
    print(f"Total videos in the playlist: {len(playlist.video_urls)}")

    # Physically downloading the audio track in MP3 format
    for video in playlist.videos:
        count += 1

        try:
            audioStream = video.streams.get_by_itag(YOUTUBE_STREAM_AUDIO)
            # Download as MP3
            audioStream.download(output_path=download_dir, filename_prefix='temp')

            # Convert the downloaded file to MP3 format
            mp4_filepath = f"{download_dir}/temp{audioStream.default_filename}"
            mp3_filepath = f"{download_dir}/{video.title}.mp3"
            print("Downloading file", count, ":", video.title)
            print(count, f"out of {len(playlist.video_urls)}")

            # You can use a library like moviepy or pydub for the conversion
            # For example, using pydub:
            audio = AudioSegment.from_file(mp4_filepath, format="mp4")
            audio.export(mp3_filepath, format="mp3")

            # Optionally, you can remove the temporary MP4 file
            os.remove(mp4_filepath)

        except exceptions.AgeRestrictedError as e:
            print(f"Skipped age-restricted video: {video.title}")
            print(f"Error message: {str(e)}")

    print("Download completed!")
