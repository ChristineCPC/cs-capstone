import { View, Text } from "react-native";
import React from "react";
import ActivityCard from "../../../src/components/activities/ActivityCard";
import { useRouter } from "expo-router";

export default function ActivitiesScreen() {
    const router = useRouter();

    return (
        <View>
            <ActivityCard 
                title="Word Bites"
                icon={<Text>🏊</Text>}
                description="Break words into smaller parts."
                color="blue"
                onPress={() => router.push(`/activities/word-bites`)}
            />

            <ActivityCard
                title="Repeat After Me"
                icon={<Text>Find smth</Text>}
                description="practice pronouncation by copying what is being said."
                color="green"
                onPress={() => router.push(`/activities/repeat-after-me`)}
            />
        </View>
    )
}