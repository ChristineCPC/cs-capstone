import {ScrollView, Text, View} from 'react-native'
import { useLocalSearchParams, useRouter } from 'expo-router'
import getActivityId from '../../../../src/activities/engine/getActivityId';
import SectionTiles from '../../../../src/components/activities/SectionTiles';

//displays activity details and sections
export default function ActivityDetails() {
    const {id} = useLocalSearchParams();
    const activity = getActivityId(id as string);
    const router = useRouter();

    return (
        <ScrollView>
            <Text>Activity Details for {activity?.name}</Text> 
            <Text>{activity?.description}</Text>
            <View>
                {activity?.sections.map((section, name) =>(
                    <SectionTiles 
                        key={name} 
                        title={section.name} 
                        onPress={() => {router.push({
                            pathname: `/(tabs)/activities/[id]/activity`,
                            params: {id: String(id), sectionId: String(section.id)}
                        });}} 
                    />
                ))}
            </View>
        </ScrollView>
    )
}