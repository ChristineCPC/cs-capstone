import {View, Text, TouchableOpacity} from "react-native";

interface ButtonProps {
    icon: React.ReactNode;
    label: string;
    onPress: () => void;
}

export default function Button({icon, label, onPress}: ButtonProps) {
    return (
        <TouchableOpacity className="bg-blue-500 rounded-lg items-center p-4" onPress={onPress}>
            <View>{icon}</View>
            <Text className="font-medium">{label}</Text>
        </TouchableOpacity>
    )
}