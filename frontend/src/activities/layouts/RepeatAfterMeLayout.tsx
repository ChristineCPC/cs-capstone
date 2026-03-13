import { Alert, Text, View } from "react-native";
import { SafeAreaView } from "react-native-safe-area-context";
import { useSafeAreaInsets } from "react-native-safe-area-context";
import Button from "@/components/Button";
import {Mic} from "lucide-react-native";
import { useState, useEffect } from "react";
import {useAudioRecorder, AudioModule, RecordingPresets, setAudioModeAsync, useAudioRecorderState} from "expo-audio";
import { sendAudioToBackend } from "@/hooks/sendAudioToBackend";

export default function RepeatAfterMeLayout() {

    const inset = useSafeAreaInsets();

    const audioRecorder = useAudioRecorder(RecordingPresets.HIGH_QUALITY);
    const recorderState = useAudioRecorderState(audioRecorder);

    const record = async () => {
        await audioRecorder.prepareToRecordAsync();
        audioRecorder.record();
    }

    const stopRecording = async () => {
        await audioRecorder.stop();
    }

    const handleRecording = async () => {
        const status = await AudioModule.requestRecordingPermissionsAsync();

        if (recorderState.isRecording) {
            await audioRecorder.stop();
            sendAudioToBackend(audioRecorder.uri as string);
            console.log("Stopped recording...");
            return;
        }

        if(!status.granted) {
            Alert.alert("Permission to access microphone was denied");
            return;
        }

        await setAudioModeAsync ({
            playsInSilentMode: true,
            allowsRecording: true,
        });

        try {
            await audioRecorder.prepareToRecordAsync();
            audioRecorder.record();
        } catch (error) {
            console.log("failed to start recording: ", error);
        }
        
    }

    return (
        <View className="items-center flex justify-between mt-10 bg-gray-500 min-h-screen">
            
            <View className="items-center">
                {/*Word Bank */}
                <View className="py-5">
                    {/*set up word bank functionality; then get a word/sentence to show up here; container length/height also needs to accomodate word/sentence length */}
                    <Text className="text-xl">Repeat after me layout: </Text>
                </View>
            
                <View className="flex-row gap-3 ">
                    {/*2-D Demonstration*/}
                    <View className="bg-red-500 w-40 h-40 justify-center">
                        <Text>AI model</Text>
                    </View>

                    {/*User Camera Feed*/}
                    <View className="bg-blue-500 w-40 h-40 justify-center">
                        <Text>User camera feed</Text>
                    </View>
                </View>
            </View>
            
            {/*Operational Buttons*/}
            <SafeAreaView className="flex-row flex-wrap justify-center gap-5 px-4 xl:mb-20 bottom-10 xl:bottom-10" style={{paddingBottom: inset.bottom}}>
                <Button icon={<Mic />} label="Record Audio" onPress={handleRecording}/>
                <Button icon={<Text>🔊</Text>} label="Play audio" onPress={handleRecording}/>
                <Button icon={<Text>🔊</Text>} label="Play audio" onPress={() => console.log("d")}/>
                <Button icon={<Text>🔊</Text>} label="Play audio" onPress={() => console.log("d")}/>
                <Button icon={<Text>🔊</Text>} label="Play audio" onPress={() => console.log("d")}/>
            </SafeAreaView>
            
        </View>

        
    )
}