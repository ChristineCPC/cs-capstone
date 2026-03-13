import {View, Text, StyleSheet, TouchableOpacity} from "react-native";

interface ActivityCardProps {
    title: string;
    icon: React.ReactNode;
    description: string;
    color: string;
    onPress: () => void;
}

export default function ActivityCard({title, icon, description, color, onPress}: ActivityCardProps) {
    return (
        <TouchableOpacity style={[styles.card, {backgroundColor: color}]} onPress={onPress}>
            <View style={styles.iconContainer}>
                {icon}
            </View>
            <Text style={styles.title}>{title}</Text>
            <Text style={styles.description}>{description}</Text>
        </TouchableOpacity>
    )
}

const styles = StyleSheet.create({
    card: {
        borderRadius: 20,
        padding: 20,
        margin: 15,
    },
    iconContainer: {},
    title: {},
    description: {},
    icon:{}
})