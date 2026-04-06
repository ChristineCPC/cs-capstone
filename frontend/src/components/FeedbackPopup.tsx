import { useState } from "react";
import { Modal, Alert, View, Text, Pressable } from "react-native";
import { SafeAreaView } from "react-native-safe-area-context";

interface feedbackProps {
    feedback: string[];
    onClose: () => void;
}

export default function FeedbackPopup({feedback, onClose}:feedbackProps) {
    return (
        <SafeAreaView>
            <Modal
                animationType="slide"
                transparent={false}
                visible={true}
                onRequestClose={() => {
                    onClose
                }}
            >
            <View className="justify-center">
                <View className="justify-center">
                    <Text className="font-bold text-xl">{feedback[0]}</Text>
                    <Text className="font-medium text-md">{feedback[1]}</Text>
                </View>
                <Pressable onPress={onClose} className=" bg-blue-400 rounded-lg p-5">
                    <Text className="font-bold text-lg color-white ">Close</Text>
                </Pressable>
            </View>
            </Modal>
        </SafeAreaView>
    );
};