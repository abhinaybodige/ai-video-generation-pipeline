from script_generator import generate_script
from voice_generator import create_voice
from visuals_fetcher import fetch_images
from video_editor import create_video


def run_pipeline(topic):

    print("Generating script...")
    script = generate_script(topic)

    print("\nScript:")
    print(script)

    print("\nGenerating voice...")
    create_voice(script)

    print("\nFetching visuals...")
    images = fetch_images(topic)

    print("\nCreating video...")
    create_video(images, "voice.mp3")

    print("\n Video generated: output.mp4")


if __name__ == "__main__":
    topic = input("Enter video topic: ")
    run_pipeline(topic)
