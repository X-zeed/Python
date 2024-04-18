#โจทย์: เขียนโปรแกรม Python เพื่อรับข้อความจากผู้ใช้แล้วแสดงผลลัพธ์เป็นข้อความที่ถูกเขียนใหญ่ทั้งหมดหรือเป็นตัวเล็กทั้งหมด
text = input()
if text.isupper():
    print(text.lower())
else:
    print(text.upper())