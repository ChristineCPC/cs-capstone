import { Tabs } from "expo-router";
import React from "react";

export default function TabLayout() {
    return (
        <Tabs
            screenOptions={{
                headerShown: false,
                tabBarActiveBackgroundColor: "blue"
            }}
        >
            <Tabs.Screen name="index" options={{title: "Home"}} />
            <Tabs.Screen name="activities" options={{title: "Activities"}} />
            <Tabs.Screen name="exercises" options={{title: "Exercises"}} />
            <Tabs.Screen name="achievements" options={{title: "Achievements"}} />
            <Tabs.Screen name="profile" options={{title: "Profile"}} />
        </Tabs>
    )
}