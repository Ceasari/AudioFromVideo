from moviepy import editor
from pathlib import Path


def extract_audio_from_video():
    """
    Prompts the user to input the path to a video file and then extracts the audio from that video,
    saving it as an MP3 file with the same name as the video file (but with an .mp3 extension).

    The function checks whether the specified file exists and is a valid file, and prints appropriate
    messages to inform the user of the process.

    No parameters or return values.
    """
    video_file_path_input = input("Please enter the path to the video file: ")
    video_file_path = Path(video_file_path_input)

    if not video_file_path.exists() or not video_file_path.is_file():
        print(f"The file {video_file_path} does not exist or is not a valid file. Please try again.")
        return

    print(f"Processing: {video_file_path}")

    video = editor.VideoFileClip(str(video_file_path))
    audio = video.audio
    audio_file_path = f'{video_file_path.stem}.mp3'
    audio.write_audiofile(audio_file_path)

    print(f"Audio extracted and saved as {audio_file_path}")


if __name__ == "__main__":
    extract_audio_from_video()

