export const fetchActivity = async (activity: string | undefined, section: string | undefined) => {
    try {
        const route = process.env.EXPO_PUBLIC_ACTIVITY_ROUTE;
        const activityRoute = route + "activity=" + activity + "&section=" + section;

        const response = await fetch(activityRoute);
        const data = await response.json();

        console.log(data);
        return data;
    } catch (error) {
        console.error("Error fetching activity: ", error);
    }
    
}