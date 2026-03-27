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
                transparent={true}
                visible={true}
                onRequestClose={() => {
                    onClose
                }}
            >
            <View>
                <View>
                    <Text>{feedback[0]}</Text>
                    <Text>{feedback[1]}</Text>
                </View>
                <Pressable onPress={onClose}>
                    <Text>Close</Text>
                </Pressable>
            </View>
            </Modal>
        </SafeAreaView>
    );
};