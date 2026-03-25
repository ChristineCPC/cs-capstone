export const fetchScore = async (activity: string | undefined, section: string | undefined) => {
    try {
        const route = process.env.EXPO_PUBLIC_SCORE_ROUTE;
        const scoreRoute = route + "activity=" + activity + "&section=" + section;

        const response = await fetch (scoreRoute);
        const data = await response.json();

        console.log(data);
        return data;
    } catch (error) {
        console.error("Error fetching score: ", error);
    }
    
}