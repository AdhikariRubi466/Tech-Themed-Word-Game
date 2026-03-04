import random
from django.shortcuts import render, redirect

# -------------------------
# Word Lists (Tech Theme)
# -------------------------

EASY_WORDS = ["mouse", "coder", "logic", "input", "print"]
MEDIUM_WORDS = ["array", "stack", "queue", "linux", "pixel"]
HARD_WORDS = ["cache", "debug", "token", "cloud", "block"]

MAX_ATTEMPTS = 6


# -------------------------
# Start Game View
# -------------------------

def start_game(request):
    if request.method == "POST":
        difficulty = request.POST.get("difficulty")

        if difficulty == "easy":
            word_list = EASY_WORDS
            multiplier = 1
        elif difficulty == "medium":
            word_list = MEDIUM_WORDS
            multiplier = 2
        else:
            word_list = HARD_WORDS
            multiplier = 3

        secret_word = random.choice(word_list)

        # Store game state in session
        request.session["secret_word"] = secret_word
        request.session["attempts"] = MAX_ATTEMPTS
        request.session["multiplier"] = multiplier
        request.session["word_list"] = word_list
        request.session["feedback"] = []
        request.session["preview_shown"] = False

        return redirect("rules")

    return render(request, "game/start.html")


# -------------------------
# Word Evaluation Logic
# (Converted from old Python)
# -------------------------

def evaluate_guess(secret_word, guess):
    result = []

    for i in range(len(guess)):
        if guess[i] == secret_word[i]:
            result.append(("correct", guess[i]))
        elif guess[i] in secret_word:
            result.append(("present", guess[i]))
        else:
            result.append(("absent", guess[i]))

    return result


# -------------------------
# Play Game View
# -------------------------

def play_game(request):
    secret_word = request.session.get("secret_word")
    attempts = request.session.get("attempts")
    multiplier = request.session.get("multiplier")
    word_list = request.session.get("word_list")
    feedback = request.session.get("feedback", [])

    # If no game exists, redirect to start
    if not secret_word:
        return redirect("start")

    # Preview control logic
    preview_shown = request.session.get("preview_shown", False)

    if not preview_shown:
        request.session["preview_shown"] = True

    if request.method == "POST":
        guess = request.POST.get("guess", "").lower()

        if len(guess) == 5:
            result = evaluate_guess(secret_word, guess)
            feedback.append(result)
            request.session["feedback"] = feedback

            # WIN CONDITION
            if guess == secret_word:
                score = attempts * 10 * multiplier
                return render(request, "game/result.html", {
                    "win": True,
                    "word": secret_word,
                    "score": score
                })

            # Reduce attempts
            attempts -= 1
            request.session["attempts"] = attempts

            # LOSE CONDITION
            if attempts == 0:
                return render(request, "game/result.html", {
                    "win": False,
                    "word": secret_word
                })

    return render(request, "game/play.html", {
        "attempts": attempts,
        "feedback": feedback,
        "word_list": word_list,
        "show_preview": not preview_shown
    })

def rules_page(request):
    if not request.session.get("secret_word"):
        return redirect("start")
    return render(request, "game/rules.html")