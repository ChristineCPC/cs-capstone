import { Stack } from "expo-router";

export default function ActivitiesLayout() {
    return (
        <Stack>
            <Stack.Screen name="index" options={{ headerTitle: "Activities", headerShown: false }} />
            <Stack.Screen name="[id]" options={{ headerTitle: "Activity Details", headerShown: false }} />
        </Stack>
    )
}