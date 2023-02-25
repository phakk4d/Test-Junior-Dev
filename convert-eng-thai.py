def eng_to_thai_number (number):
    thai_numbers = {
        "zero" : "ศูนย์",
        "one" : "หนึ่ง",
        "two" : "สอง",
        "three" : "สาม",
        "four" : "สี่",
        "five" : "ห้า",
        "six" : "หก",
        "seven" : "เจ็ด",
        "eight" : "แปด",
        "nine" : "เก้า",
        "ten" : "สิบ",
        "eleven" : "สิบเอ็ด",
        "twelve" : "สิบสอง",
        "thirteen" : "สิบสาม",
        "fourteen" : "สิบสี่",
        "fifteen" : "สิบห้า",
        "sixteen" : "สิบหก",
        "seventeen" : "สิบเจ็ด",
        "eighteen" : "สิบแปด",
        "nineteen" : "สิบเก้า",
        "twenty" : "ยี่สิบ",
        "twenty one" : "ยี่สิบเอ็ด",
        "thirty" : "สามสิบ",
        "thirty one" : "สามสิบเอ็ด",
        "forty" : "สี่สิบ",
        "forty one" : "สี่สิบเอ็ด",
        "fifty" : "ห้าสิบ",
        "fifty one" : "ห้าสิบเอ็ด",
        "sixty" : "หกสิบ",
        "sixty one" : "หกสิบเอ็ด",
        "seventy" : "เจ็ดสิบ",
        "seventy one" : "เจ็ดสิบเอ็ด",
        "eighty" : "แปดสิบ",
        "eighty one" : "แปดสิบเอ็ด",
        "ninety" : "เก้าสิบ",
        "ninety one" : "เก้าสิบเอ็ด",
        "hundred" : "ร้อย",
        "thousand" : "พัน",
        "baht" : "บาท",
        "only" : "ถ้วน"
    }

    if number == 0 :
        return thai_numbers["zero"]
    
    words = number.lower().split()
    thai_words = [thai_numbers[word] for word in words]
    return "".join(thai_words)

print (eng_to_thai_number("one thousand baht only"))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       