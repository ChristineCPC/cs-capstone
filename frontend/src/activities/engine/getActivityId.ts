import {configs} from "../configs";

export default function getActivityId(id: string) {
    return configs.find((activity) => activity.id === id);
}