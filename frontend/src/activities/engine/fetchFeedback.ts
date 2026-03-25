export const fetchFeedback = async (activity: string | undefined, section: string | undefined) => {
    try {
        const route = process.env.EXPO_PUBLIC_FEEDBACK_ROUTE;
        const feedbackRoute = route + "activity=" + activity + "&section=" + section;

        const response = await fetch(feedbackRoute);
        const data = await response.json();

        console.log(data);
        return data;
    } catch (error) {
        console.error("Error fetching feedback: ", error);
    }
    
}