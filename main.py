from writer import generate_ig_captions

if __name__ == "__main__":
    topic = input("請輸入 IG 貼文主題：")
    results = generate_ig_captions(topic)

    for style, text in results.items():
        print(f"\n📝 風格：{style}\n{text}\n")
