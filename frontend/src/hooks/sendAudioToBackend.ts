export const sendAudioToBackend = async (uri: string) => {
    {/*Send audio to agent in backend; Agent sends data back to frontend*/}
    
    const formData = new FormData();

    const fileConfig: any = {
        uri: uri,
        type: "audio/wav",
        name: "recording.wav",
    };

    formData.append("audio_file", fileConfig);

    const agentRoute = process.env.EXPO_PUBLIC_AGENT_ROUTE;

    const response = await fetch(agentRoute, {
        method: "POST",
        body: formData,
        headers: {"Accept": "application/json"},
    });

    const data = await response.json();
    console.log(data.transcription)
    return data;
}

