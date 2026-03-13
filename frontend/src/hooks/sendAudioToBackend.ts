export const sendAudioToBackend = async (uri: string) => {
    const formData = new FormData();

    const fileConfig: any = {
        uri: uri,
        type: "audio/wav",
        name: "recording.wav",
    };

    formData.append("audio_file", fileConfig);

    const transcriptRoute = process.env.EXPO_PUBLIC_TRANSCRIPT_ROUTE;

    const response = await fetch(transcriptRoute, {
        method: "POST",
        body: formData,
        headers: {"Accept": "application/json"},
    });

    const data = await response.json();
    console.log(data.transcription)
}

