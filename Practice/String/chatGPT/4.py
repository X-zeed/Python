#โจทย์: เขียนโปรแกรม Python เพื่อรับข้อความจากผู้ใช้แล้วแสดงผลลัพธ์เป็นจำนวนตัวอักษรต่างๆที่ปรากฎในข้อความพร้อมกับจำนวนครั้งที่ปรากฎ
text = input()
for letter in text:
    print(letter , text.count(letter))