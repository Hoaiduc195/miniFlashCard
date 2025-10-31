import json

def txt_to_flashcards(input_path, output_path):
    flashcards = []

    with open(input_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if "||" in line:
                front, back = line.split("||", 1)
                flashcards.append({
                    "front": front.strip(),
                    "back": back.strip()
                })

    data = {"flashcards": flashcards}

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Converted to JSON: {output_path}")

# --- Ví dụ sử dụng ---
# txt_to_flashcards("vocab.txt", "flashcards.json")
