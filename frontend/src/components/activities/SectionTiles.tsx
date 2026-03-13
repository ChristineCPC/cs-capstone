import {View, Text, StyleSheet, TouchableOpacity} from "react-native";

interface SectionTilesProps {
    title: string;
    onPress: () => void;
}

export default function SectionTiles({title, onPress}: SectionTilesProps) {
    return (
        <TouchableOpacity style={[styles.tile]} onPress={onPress}>
            <Text style={styles.title}>{title}</Text>
        </TouchableOpacity>
    )
}

const styles = StyleSheet.create({
    tile: {
        borderRadius: 20,
        padding: 20,
        margin: 15,
       backgroundColor: "blue",
    },
    title: {},
})