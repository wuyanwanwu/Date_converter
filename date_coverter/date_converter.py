import tkinter as tk
from tkinter import messagebox
import datetime
import re


# 日期格式解析函数
def parse_date(input_date):
    formats = [
        (r'^\d{8}$', '%Y%m%d'),  # YYYYmmdd
        (r'^\d{4}-\d{2}-\d{2}$', '%Y-%m-%d'),  # YYYY-mm-dd
        (r'^\d{4}/\d{2}/\d{2}$', '%Y/%m/%d'),  # YYYY/mm/dd
        (r'^\d{2}/\d{2}/\d{4}$', '%m/%d/%Y'),  # mm/dd/YYYY
        (r'^\d{4}\d{3}$', '%Y%j'),  # YYYYddd
        (r'^\d{4}-\d{3}$', '%Y-%j'),  # YYYY-ddd
    ]

    for pattern, date_format in formats:
        if re.match(pattern, input_date):
            return datetime.datetime.strptime(input_date, date_format)

    raise ValueError("Unsupported date format")


# 公历转儒日历函数
def to_julian(date):
    return date.strftime('%Y%j')  # 返回格式为 YYYYddd


# 儒日历转公历函数
def from_julian(julian_date):
    date = parse_date(julian_date)
    return date.strftime('%Y-%m-%d')  # 转换回 YYYY-mm-dd 格式


# 转换函数
def convert_date(event=None):  # 允许接受回车事件
    input_date = entry.get().strip()
    try:
        if re.match(r'^\d{4}\d{3}$|^\d{4}-\d{3}$', input_date):
            result = from_julian(input_date)
            output_var.set(f"转换后的公历日期: {result}")
        else:
            date = parse_date(input_date)
            julian_date = to_julian(date)
            output_var.set(f"转换后的儒日历: {julian_date}")
    except ValueError as e:
        messagebox.showerror("错误", str(e))


# 创建 GUI
root = tk.Tk()
root.title("公历与儒日历转换器")

# 设置窗口大小
window_width = 600
window_height = 300

# 获取屏幕尺寸
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# 计算窗口居中的位置
position_top = int((screen_height - window_height) / 2)
position_right = int((screen_width - window_width) / 2)

# 设置窗口初始位置为屏幕正中
root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

# 输入框
entry_label = tk.Label(root, text="请输入日期:", font=('Arial', 12))
entry_label.pack(pady=10)

entry = tk.Entry(root, width=40, font=('Arial', 12))
entry.pack(pady=10)

# 绑定回车键
entry.bind('<Return>', convert_date)

# 转换按钮
convert_button = tk.Button(root, text="转换", command=convert_date, font=('Arial', 12))
convert_button.pack(pady=10)

# 输出结果
output_var = tk.StringVar()
output_label = tk.Label(root, textvariable=output_var, font=('Arial', 12))
output_label.pack(pady=10)

# 启动 GUI
root.mainloop()
