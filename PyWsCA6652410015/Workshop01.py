def countword(sentence):
    words = sentence.split()
    totalWords = len(words)
    
    uniqueWords = set(words)
    totalUnique = len(uniqueWords)
    
    duplicateWords = [word for word in uniqueWords if words.count(word) > 1]
    
    print(f"มีคำรวมทั้งหมด {totalWords} คำ")
    print(f"มีคำที่ซ้ำกันรวม {len(duplicateWords)} คำ คือ {' '.join(duplicateWords)}")
    
    for word in duplicateWords:
        count = words.count(word)
        print(f"คำว่า {word} ซ้ำกัน {count} ครั้ง")

try:
    inputword = input("ป้อนข้อความ: ")
    countword(inputword)
except Exception as e:
    print(f"เกิดข้อผิดพลาด: {e}")