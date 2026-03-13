import { Stack } from "expo-router";

export default function ActivityIdLayout() {
    return (
        <Stack>
            <Stack.Screen name="index" options={{ headerTitle: "Activity Details", headerShown: false }} />
            <Stack.Screen name="activity" options={{ headerTitle: "Current Activity", headerShown: false }} />
        </Stack>
    )
}