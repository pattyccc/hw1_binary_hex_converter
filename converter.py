import tkinter as tk
from tkinter import messagebox

# --- 核心邏輯區 (不使用內建函式) ---

def dec_to_bin(n):
    '''將 0-255 的 10 進位轉為 2 進位字串'''
    if n == 0: return "0"
    res = ""
    temp = n
    while temp > 0:
        res = str(temp % 2) + res
        temp //= 2
    return res.zfill(8) # 補齊 8 位

def dec_to_hex(n):
    '''將 0-255 的 10 進位轉為 16 進位字串'''
    if n == 0: return "0"
    hex_chars = "0123456789ABCDEF"
    res = ""
    temp = n
    while temp > 0:
        res = hex_chars[temp % 16] + res
        temp //= 16 # 修正：這裡應該是除以 16
    return res

def bin_to_dec(b_str):
    '''2 進位字串轉 10 進位'''
    res = 0
    for i, char in enumerate(reversed(b_str)):
        if char == '1':
            res += (2 ** i)
    return res

# --- GUI 介面區 (在 Colab 環境中無法直接運行，因為 Colab 沒有圖形顯示界面) ---
# 這些代碼塊將被註釋掉，以便程序可以在 Colab 中執行其核心邏輯

# class ConverterApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("HW1: 進位轉換器 (0-255)")
#         self.root.geometry("300x250")

#         # 10 進位輸入
#         tk.Label(root, text="10 進位 (Decimal):").pack(pady=5)
#         self.ent_dec = tk.Entry(root)
#         self.ent_dec.pack()

#         # 轉換按鈕
#         tk.Button(root, text="開始轉換", command=self.perform_conversion).pack(pady=10)

#         # 結果顯示
#         self.lbl_bin = tk.Label(root, text="2 進位: ", fg="blue")
#         self.lbl_bin.pack()

#         self.lbl_hex = tk.Label(root, text="16 進位: ", fg="green")
#         self.lbl_hex.pack()

#     def perform_conversion(self):
#         try:
#             val = int(self.ent_dec.get())
#             if 0 <= val <= 255:
#                 b_result = dec_to_bin(val)
#                 h_result = dec_to_hex(val)
#                 self.lbl_bin.config(text=f"2 進位: {b_result}")
#                 self.lbl_hex.config(text=f"16 進位: {h_result}")
#             else:
#                 messagebox.showerror("錯誤", "請輸入 0-255 之間的數字")
#         except ValueError:
#             messagebox.showerror("錯誤", "請輸入有效的整數")

if __name__ == "__main__":
    # root = tk.Tk()
    # app = ConverterApp(root)
    # root.mainloop()
    print("--- 核心轉換邏輯測試 ---")
    test_decimal = 255
    print(f"10 進位: {test_decimal}")
    print(f"2 進位: {dec_to_bin(test_decimal)}")
    print(f"16 進位: {dec_to_hex(test_decimal)}")

    test_decimal_2 = 10
    print(f"
10 進位: {test_decimal_2}")
    print(f"2 進位: {dec_to_bin(test_decimal_2)}")
    print(f"16 進位: {dec_to_hex(test_decimal_2)}")

    test_binary = "11111111"
    print(f"
2 進位: {test_binary}")
    print(f"轉換為 10 進位: {bin_to_dec(test_binary)}")

    test_binary_2 = "1010"
    print(f"
2 進位: {test_binary_2}")
    print(f"轉換為 10 進位: {bin_to_dec(test_binary_2)}")

    print("
注意：Tkinter GUI 在 Google Colab 環境中無法直接運行，因為 Colab 缺乏圖形顯示界面。")
    print("您可以運行此單元格來測試核心轉換邏輯。")
