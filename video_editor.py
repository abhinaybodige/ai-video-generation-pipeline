from moviepy import ImageClip, AudioFileClip, concatenate_videoclips


def create_video(images, audio_file, output="output.mp4"):

    audio = AudioFileClip(audio_file)
    duration_per_image = audio.duration / len(images)

    clips = []

    for img in images:
        clip = (
            ImageClip(img)
            .with_duration(duration_per_image)
            .resized((1280, 720))
            .with_fps(24)
        )
        clips.append(clip)

    video = concatenate_videoclips(clips, method="compose")
    video = video.with_audio(audio)

    video.write_videofile(
        output,
        codec="libx264",
        audio_codec="aac"
    )
