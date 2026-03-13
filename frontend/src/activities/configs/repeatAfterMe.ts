import RepeatAfterMeLayout from "../layouts/RepeatAfterMeLayout";

export const repeatAfterMeConfig = {
    id: "repeat-after-me",
    name: "Repeat After Me",
    description: "Practice pronunciation by copying what is being said.",
    sections: [
        {id: "at-words", name: "-at Words", layout: RepeatAfterMeLayout},
        {id: "short-sentences", name: "Short Sentences", layout: RepeatAfterMeLayout}
    ],
    engine: {},
    inputs: ['audio'],
    logic: {},
    session: []
}