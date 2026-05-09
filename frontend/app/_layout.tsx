import "../global.css";
import {Stack} from "expo-router";
import { StatusBar } from "react-native";
import { SafeAreaProvider } from "react-native-safe-area-context";

export default function App() {
    return (
        <SafeAreaProvider>
            <StatusBar />
            <Stack>
                <Stack.Screen name="(tabs)" options={{headerShown: false}} />
            </Stack>
        </SafeAreaProvider>
    );
}