import edge_tts
import asyncio

async def generate_voice(script, output_file="voice.mp3"):
    communicate = edge_tts.Communicate(
        script,
        voice="en-IN-NeerjaNeural"  # Indian female voice
    )

    await communicate.save(output_file)

def create_voice(script):
    asyncio.run(generate_voice(script))
