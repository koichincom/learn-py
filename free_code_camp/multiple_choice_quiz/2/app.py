from question import Prompt_and_answer

question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

quizzes = [
    Prompt_and_answer(question_prompts[0], "a"),
    Prompt_and_answer(question_prompts[1], "c"),
    Prompt_and_answer(question_prompts[2], "b")
]

def run_test(quizzes):
    i = 0
    for text in quizzes:
        answer = input(text.prompt)
        if answer == Prompt_and_answer.answer:
            i += 1
    print(f"You got {i}/{len(quizzes)} correct")

run_test(quizzes)