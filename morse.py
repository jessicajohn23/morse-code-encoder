import time
import winsound

# Morse Code Dictionary
MORSE = {
    'A': '.-',   'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.',    'F': '..-.', 'G': '--.',  'H': '....',
    'I': '..',   'J': '.---', 'K': '-.-',  'L': '.-..',
    'M': '--',   'N': '-.',   'O': '---',  'P': '.--.',
    'Q': '--.-', 'R': '.-.',  'S': '...',  'T': '-',
    'U': '..-',  'V': '...-', 'W': '.--',  'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', '!': '-.-.--',
    '/': '-..-.', ' ': '/'
}

# Timing (ITU standard)
FREQUENCY = 700    #Hz
DOT_TIME = 0.1    #seconds
DASH_TIME = DOT_TIME*3
GAP_SYMBOL = DOT_TIME
GAP_LETTER = DOT_TIME*3
GAP_WORD = DOT_TIME * 7

def play_symbol(symbol):
    duration = DOT_TIME if symbol == '.' else DASH_TIME
    winsound.Beep(FREQUENCY, int(duration * 1000))  #(winsound takes milliseconds)
    time.sleep(GAP_SYMBOL)

# ── Encode & Transmit ──────────────────────────────────────────────
def text_to_morse(text):
    result = []
    for char in text.upper():
        if char in MORSE:
            result.append(MORSE[char])
        else:
            result.append('?')
    return ' '.join(result)

def transmit(text):
    print(f"\n  Input : {text}")
    morse_str = text_to_morse(text)
    print(f"  Morse : {morse_str}")
    print(f"\n  Transmitting", end='', flush=True)

    for char in text.upper():
        if char == ' ':
            print(' / ', end='', flush=True)
            time.sleep(GAP_WORD)
            continue

        if char not in MORSE:
            print(f' [?]', end='', flush=True)
            continue

        code = MORSE[char]
        print(f' {code}', end='', flush=True)

        for symbol in code:
            play_symbol(symbol)

        time.sleep(GAP_LETTER)

    print('\n\n  ✓ Done!\n')

# Main Loop
def main():
    print("=" * 40)
    print("   MORSE CODE ENCODER")
    print("=" * 40)
    print("  Supports: A-Z, 0-9, . , ? ! /")
    print("  Type 'quit' to exit\n")

    while True:
        try:
            text = input("  Enter text: ").strip()
            if not text:
                continue
            if text.lower() == 'quit':
                print("  Goodbye!")
                break
            transmit(text)
        except KeyboardInterrupt:
            print("\n  Interrupted. Goodbye!")
            break

if __name__ == "__main__":
    main()