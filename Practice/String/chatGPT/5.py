#โจทย์: เขียนโปรแกรม Python เพื่อรับข้อความจากผู้ใช้แล้วตรวจสอบว่าข้อความนั้นเป็น palindrome หรือไม่
text = input()
if text == text[::-1]:
    print("True")
else:
    print("False")