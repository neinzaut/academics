import time
import random

# --- Game State ---
inventory = []
mood_score = 50  # 0 = bad, 100 = excellent

def delay(seconds=1.5):
    time.sleep(seconds)

def letter_delay(text, delay_time=0.04):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay_time)
    print()

# --- Utility Functions ---
def adjust_mood(amount):
    global mood_score
    mood_score = max(0, min(100, mood_score + amount))
    print(f"(🧠 Mood score is now {mood_score}.)")
    delay()

def get_emotion():
    delay()
    emotion = input("\nHow are you feeling right now? (happy, sad, angry, bored): ").lower()
    if emotion not in ["happy", "sad", "angry", "bored"]:
        print("Your feelings are hard to place. But they still shape the world.")
        return "neutral"
    return emotion

# --- Scene 1: Introduction ---
def scene_intro(emotion):
    letter_delay("\n🌫 Welcome to the Realm of Echoes...")
    delay(2)

    if emotion == "happy":
        print("☀️ The sun shines brightly. Echoes of laughter ripple through the forest.")
        adjust_mood(10)
    elif emotion == "sad":
        print("🌧 Rain drizzles gently. You wander through a misty moor, memories whispering in the fog.")
        adjust_mood(-10)
    elif emotion == "angry":
        print("🌩 Thunder crackles overhead. You stand before a shattered battlefield, fists clenched.")
        adjust_mood(-15)
    elif emotion == "bored":
        print("🌾 You sit in a field of still grass. The world feels unmoving. Empty.")
        adjust_mood(-5)
    else:
        print("🌫 A shapeless landscape surrounds you, echoing your uncertain heart.")

# --- Scene 2: Choose Path ---
def scene_choose_path(emotion):
    letter_delay("\n⚔️ A fork splits the road ahead:")
    delay()
    print("1. Walk toward the glowing forest.")
    print("2. Explore the ruins to the east.")
    print("3. Sit and observe the surroundings.")
    choice = input("Enter 1, 2 or 3: ")

    if choice == "1":
        return scene_forest(emotion)
    elif choice == "2":
        return scene_ruins(emotion)
    elif choice == "3":
        letter_delay("You wait in silence. A bird chirps nearby.")
        adjust_mood(5)
        return "meadow"
    else:
        letter_delay("\nYou hesitate too long. The world warps around you...")
        delay()
        return "unknown"

# --- Scene 3A: Forest Exploration ---
def scene_forest(emotion):
    letter_delay("\n🌳 The forest embraces you with shifting light.")
    delay()

    if emotion == "happy":
        letter_delay("✨ A glowing butterfly leads you to a hidden grove. You find a healing herb.")
        inventory.append("healing herb")
        adjust_mood(10)
    elif emotion == "angry":
        letter_delay("🐾 A beast attacks. You fight back, but you're wounded.")
        adjust_mood(-20)
    else:
        letter_delay("🔮 You discover a broken pendant with your initials.")
        inventory.append("old pendant")
        adjust_mood(-5)
    return "forest"

# --- Scene 3B: Ruins Encounter ---
def scene_ruins(emotion):
    letter_delay("\n🏛 Cracked stone walls whisper forgotten names.")
    delay()
    print("An old man named Coren emerges from shadow.")
    delay()

    if emotion == "sad":
        letter_delay("Coren places a gentle hand on your shoulder. 'You've lost much, haven't you?'")
        adjust_mood(10)
    elif emotion == "angry":
        letter_delay("Coren narrows his eyes. 'Tame your fire, or it will consume you.'")
        adjust_mood(-5)
    else:
        letter_delay("Coren studies you, then offers a map.")
        inventory.append("ancient map")
        adjust_mood(5)

    letter_delay("\nWhat do you do?")
    print("1. Ask Coren about the ruins.")
    print("2. Trade with Coren.")
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        letter_delay("\n🗿 'These stones hold echoes of lives lost. Touch them to remember.'")
        adjust_mood(5)
    elif choice == "2":
        if "healing herb" in inventory:
            print("You trade the herb for a memory shard.")
            inventory.remove("healing herb")
            inventory.append("memory shard")
        else:
            print("You have nothing Coren wants.")
    return "ruins"

# --- Scene 4: The Gate ---
def scene_gate(emotion):
    letter_delay("\n🚪 You arrive at a shimmering, humming gate.")
    delay()

    if "memory shard" in inventory:
        print("The shard vibrates and dissolves. The gate opens.")
        adjust_mood(10)
    else:
        print("The gate remains sealed. Something personal is missing.")
        adjust_mood(-5)

    print("\nDo you:")
    print("1. Try to force the gate open.")
    print("2. Meditate and search for memory.")
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        if emotion == "angry":
            letter_delay("You punch it. Cracks appear, but your hand bleeds.")
            adjust_mood(-10)
        else:
            letter_delay("You push, but nothing moves.")
            adjust_mood(-5)
    elif choice == "2":
        letter_delay("🌌 A memory awakens: a sibling's voice, a broken promise, a distant home.")
        inventory.append("core memory")
        adjust_mood(20)

# --- Scene 5: Ending ---
def scene_ending():
    letter_delay("\n📜 Final Inventory:")
    for item in inventory:
        print(f"- {item}")
    print(f"\n🧠 Final Mood Score: {mood_score}")
    delay(2)

    letter_delay("\n🌀 You reach the heart of the Realm of Echoes.")
    delay()

    if "core memory" in inventory:
        letter_delay("💡 The pieces of your past fall into place. You remember who you were.")
    else:
        letter_delay("🌑 Your memories remain scattered... but the journey has changed you.")
    print("\n— End of Chapter One —")

# --- Game Controller ---
def main():
    global inventory, mood_score

    # Scene 1
    emotion = get_emotion()
    scene_intro(emotion)

    # Scene 2
    path = scene_choose_path(emotion)

    # Scene 3
    emotion = get_emotion()
    scene_gate(emotion)

    # Ending
    scene_ending()

if __name__ == "__main__":
    main()
