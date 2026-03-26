import { useState } from "react";
import { Modal, Alert, View, Text, Pressable } from "react-native";
import { SafeAreaView } from "react-native-safe-area-context";

interface feedbackProps {
    feedback: string[];
}

export default function FeedbackPopup({feedback}:feedbackProps) {
    const [feedbackVisible, setFeedbackVisible] = useState(false);
    return (
        <SafeAreaView>
            <Modal
                animationType="slide"
                transparent={true}
                visible={feedbackVisible}
                onRequestClose={() => {
                    Alert.alert('Popup has been closed...');
                    setFeedbackVisible(!feedbackVisible)
                }}
            >
            <View>
                <View>
                    <Text>{feedback[0]}</Text>
                    <Text>{feedback[1]}</Text>
                </View>
                <Pressable>
                    <Text>Close</Text>
                </Pressable>
            </View>
            </Modal>
        </SafeAreaView>
    )
}