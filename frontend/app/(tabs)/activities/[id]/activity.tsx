import getActivityId from "../../../../src/activities/engine/getActivityId";
import { useLocalSearchParams } from "expo-router";
import { Text, View } from "react-native";
import { useSafeAreaInsets } from "react-native-safe-area-context";
import { SafeAreaView } from "react-native-safe-area-context";

export default function ActivityScreen() {
    const {id, sectionId} = useLocalSearchParams();
    //const section = getSectionId(id as string);
    const activity = getActivityId(id as string);
    const section = activity?.sections.find(s => s.id === sectionId);
    const LayoutComponent = section?.layout;
    //const insets = useSafeAreaInsets();

    return (

        <SafeAreaView className="flex-col">

            {/*Header*/}
            <View className="bg-red-500 h-20 p-5 top-0 absolute w-full">
                <Text className="text-xl font-bold">{activity?.name} - {section?.name}</Text>
            </View>
            
            {/*Activity UI*/}
            <View>
                {LayoutComponent && (<LayoutComponent />)}
            </View>
        </SafeAreaView>
    )
}
