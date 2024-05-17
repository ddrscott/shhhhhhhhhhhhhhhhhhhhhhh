from openai import OpenAI

def transcribe(src):
    """
    Transcribe an audio file to text.
    """

    client = OpenAI()

    return client.audio.transcriptions.create(
        model="whisper-1",
        file=src,
        prompt="Segment the speakers in the audio along with the text spoken by each speaker.",
    )
