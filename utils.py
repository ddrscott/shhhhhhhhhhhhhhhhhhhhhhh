def transcribe(src):
    """
    Transcribe an audio file to text.
    """

    from openai import OpenAI

    client = OpenAI()

    return client.audio.transcriptions.create(
        model="whisper-1",
        file=src,
        prompt="Segment the speakers in the audio along with the text spoken by each speaker.",
    )
