import { Alert, Text, View } from "react-native";
import { SafeAreaView } from "react-native-safe-area-context";
import { useSafeAreaInsets } from "react-native-safe-area-context";
import Button from "@/components/Button";
import {Mic} from "lucide-react-native";
import { useState, useEffect } from "react";
import {useAudioRecorder, AudioModule, RecordingPresets, setAudioModeAsync, useAudioRecorderState} from "expo-audio";
import { sendAudioToBackend } from "@/hooks/sendAudioToBackend";
import { Router, useLocalSearchParams } from "expo-router";
import getActivityId from "../engine/getActivityId";
import { fetchActivity } from "../engine/fetchActivities";

export default function RepeatAfterMeLayout() {

    const {id, sectionId} = useLocalSearchParams();
    const activity = getActivityId(id as string);
    const section = activity?.sections.find(s => s.id === sectionId);

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

    const [bank, setBank] = useState<string[]>([]);
    const [currentIndex, setCurrentIndex] = useState(0);

    useEffect(() => {
        const handleActivities = async () => {
            if (!activity?.id || !section?.id) return;

            const currentActivity = await fetchActivity(activity?.id, section?.id);

            const difficultyLevel = "1";

            const fetchBank = currentActivity?.[difficultyLevel] || [];
            setBank(fetchBank);
            setCurrentIndex(0);
        };

        handleActivities();
    }, [activity, section])

    const onDisplay = bank[currentIndex];

    return (
        <View className="items-center flex justify-between mt-10 bg-gray-500 min-h-screen p-10">
            
            <View className="items-center">
                {/*Word Bank */}
                <View className="py-5">
                    {/*set up word bank functionality; then get a word/sentence to show up here; container length/height also needs to accomodate word/sentence length */}
                    <Text className="text-xl">{activity?.name} - {section?.name} Layout</Text>
                </View>
            
                <View className="flex flex-row flex-wrap mx-20">
                    <View className="w-2/5 p-2">
                        {/*2-D Demonstration*/}
                        <View className="bg-red-500 h-60 justify-center">
                            <Text>AI model</Text>
                        </View>
                    </View>

                    <View className="w-3/5 p-2">
                        {/*Word/Sentence Bank*/}
                        <View className="bg-blue-500 h-60 justify-center">
                            <View className="p-10">
                                <Text className="text-5xl font-bold uppercase">{onDisplay ? onDisplay: "Loading..."}</Text>
                            </View>
                        </View>
                    </View>
                </View>
            </View>
            
            {/*Operational Buttons*/}
            <SafeAreaView className="flex-row flex-wrap justify-center gap-5 px-4 xl:mb-10 bottom-0 xl:bottom-20" style={{paddingBottom: inset.bottom}}>
                <Button icon={<Mic />} label="Record Audio" onPress={handleRecording}/>
                <Button icon={<Text>🔊</Text>} label="Record Audio" onPress={handleRecording}/>
                <Button icon={<Text>🔊</Text>} label="Replay Demo" onPress={() => console.log("d")}/>
                <Button icon={<Text>🔊</Text>} label="Play audio" onPress={() => console.log("d")}/>
                <Button icon={<Text>🔊</Text>} label="Play audio" onPress={() => console.log("d")}/>
            </SafeAreaView>
            
        </View>

        
    )
}