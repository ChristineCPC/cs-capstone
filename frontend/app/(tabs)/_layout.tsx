import { Tabs } from "expo-router";
import React from "react";
import {Home, Activity, Dumbbell, Trophy, User} from "lucide-react-native";

export default function TabLayout() {
    return (
        <Tabs
            screenOptions={{
                headerShown: false,
                tabBarActiveBackgroundColor: "white",
                tabBarInactiveBackgroundColor: "orange",
                tabBarActiveTintColor: "black",
                tabBarInactiveTintColor: "white",
                tabBarLabelStyle: {fontSize: 12, fontWeight: "bold"}
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