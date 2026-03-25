# hw1_binary_hex_converter
import tkinter as tk
from tkinter import messagebox

class ConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Binary / Decimal / Hex Converter")
        
        # UI 佈局
        tk.Label(root, text="Binary").grid(row=0, column=0)
        tk.Label(root, text="Decimal").grid(row=0, column=1)
        tk.Label(root, text="Hexadecimal").grid(row=0, column=2)
        
        self.bin_entry = tk.Entry(root)
        self.dec_entry = tk.Entry(root)
        self.hex_entry = tk.Entry(root)
        
        self.bin_entry.grid(row=1, column=0, padx=5, pady=5)
        self.dec_entry.grid(row=1, column=1, padx=5, pady=5)
        self.hex_entry.grid(row=1, column=2, padx=5, pady=5)
        
        tk.Button(root, text="Convert", command=self.convert, width=40).grid(row=2, column=0, columnspan=3, pady=10)
        tk.Button(root, text="Clear", command=self.clear, width=40).grid(row=3, column=0, columnspan=3)

    # 手動實作：十進位轉二進位 (依據講義方法)
    def dec_to_bin(self, n):
        if n == 0: return "0"
        res = ""
        # 為了支援超過 255 (2^8)，我們動態找起始次方
        power = 0
        while (2 ** (power + 1)) <= n:
            power += 1
        
        temp = n
        for i in range(power, -1, -1):
            val = 2 ** i
            if temp >= val:
                res += "1"
                temp -= val
            else:
                res += "0"
        return res

    # 手動實作：二進位轉十進位
    def bin_to_dec(self, b_str):
        res = 0
        for i, bit in enumerate(b_str[::-1]):
            if bit == '1':
                res += (2 ** i)
        return res

    # 手動實作：十進位轉十六進位
    def dec_to_hex(self, n):
        if n == 0: return "0"
        hex_chars = "0123456789ABCDEF"
        res = ""
        temp = n
        while temp > 0:
            res = hex_chars[temp % 16] + res
            temp //= 16
        return res

    # 手動實作：十六進位轉十進位
    def hex_to_dec(self, h_str):
        hex_chars = "0123456789ABCDEF"
        h_str = h_str.upper()
        res = 0
        for i, char in enumerate(h_str[::-1]):
            val = hex_chars.find(char)
            res += val * (16 ** i)
        return res

    def convert(self):
        try:
            # 判斷哪個欄位有輸入
            if self.dec_entry.get():
                d = int(self.dec_entry.get())
                self.bin_entry.delete(0, tk.END)
                self.bin_entry.insert(0, self.dec_to_bin(d))
                self.hex_entry.delete(0, tk.END)
                self.hex_entry.insert(0, self.dec_to_hex(d))
                
            elif self.bin_entry.get():
                b = self.bin_entry.get()
                d = self.bin_to_dec(b)
                self.dec_entry.delete(0, tk.END)
                self.dec_entry.insert(0, str(d))
                self.hex_entry.delete(0, tk.END)
                self.hex_entry.insert(0, self.dec_to_hex(d))
                
            elif self.hex_entry.get():
                h = self.hex_entry.get()
                d = self.hex_to_dec(h)
                self.dec_entry.delete(0, tk.END)
                self.dec_entry.insert(0, str(d))
                self.bin_entry.delete(0, tk.END)
                self.bin_entry.insert(0, self.dec_to_bin(d))
        except ValueError:
            messagebox.showerror("Error", "請輸入有效的數字")

    def clear(self):
        self.bin_entry.delete(0, tk.END)
        self.dec_entry.delete(0, tk.END)
        self.hex_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ConverterApp(root)
    root.mainloop()
    
