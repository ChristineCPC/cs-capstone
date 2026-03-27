export const sendAudioToBackend = async (uri: string, currentWord: string) => {
    {/*Send audio and currentWord to agent in backend; Agent sends data back to frontend*/}
    
   try {
     const formData = new FormData();

        const fileConfig: any = {
            uri: uri,
            type: "audio/m4a",
            name: "recording.m4a",
        };

        formData.append("audio_file", fileConfig);
        formData.append("current_word", currentWord);

        const agentRoute = process.env.EXPO_PUBLIC_AGENT_ROUTE;

        const response = await fetch(agentRoute, {
            method: "POST",
            body: formData,
            headers: {"Accept": "application/json"},
        });

        if (!response.ok) {
            const errorMsg = await response.text();
            console.error("Backend Error: ", errorMsg);
            throw new Error(`Backend returned ${response.status}`);
        }

        const data = await response.json();

        return data;
   } catch (error) {
        console.log("Error sending audio...", error);
        return {
            transcript: "",
            score: 0,
            feedback: []
        };
   }
};

