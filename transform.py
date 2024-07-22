from moviepy.editor import *
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

def create_video(image_path, audio_path, output_path, fps=24):
    # Load the image
    image_clip = ImageClip(image_path)

    # Load the audio
    audio_clip = AudioFileClip(audio_path)

    # Set the duration of the image to match the audio duration
    image_clip = image_clip.set_duration(audio_clip.duration)

    # Set the audio of the image clip
    image_clip = image_clip.set_audio(audio_clip)

    # Set the fps of the image clip
    image_clip = image_clip.set_fps(fps)

    # Write the result to a file
    image_clip.write_videofile(output_path, codec='libx264', audio_codec='aac', fps=fps)

# Example usage
image_path = 'image.png'
audio_path = 'Aufnahme.mp3'
output_path = 'output_video.mp4'

create_video(image_path, audio_path, output_path)
