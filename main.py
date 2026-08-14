import tkinter as tk
from tkinter import messagebox


class SendarLiteApp:

  def __init__(self, root):
    self.root = root
    self.root.title("Sendar Lite - نظام الإدارة والتحكم")
    self.root.geometry("350x500")
    self.root.config(bg="#f4f4f4")

    # عنوان التطبيق
    title_label = tk.Label(
        root,
        text="منصة Sendar المصغرة",
        font=("Arial", 16, "bold"),
        bg="#f4f4f4",
        fg="#333",
    )
    title_label.pack(pady=20)

    # حقل إدخال البيانات أو الرسالة
    self.msg_label = tk.Label(
        root, text="أدخل النص أو الأمر:", bg="#f4f4f4", font=("Arial", 11)
    )
    self.msg_label.pack(anchor="w", padx=25)

    self.entry = tk.Entry(root, font=("Arial", 12), width=28)
    self.entry.pack(pady=5, padx=20)

    # زر تنفيذ العملية
    action_btn = tk.Button(
        root,
        text="تشغيل العملية",
        font=("Arial", 12, "bold"),
        bg="#4CAF50",
        fg="white",
        width=22,
        command=self.run_process,
    )
    action_btn.pack(pady=15)

    # شاشة النتائج أو سجل العمليات
    self.log_box = tk.Text(root, height=10, width=32, font=("Courier", 10))
    self.log_box.pack(pady=10)
    self.log_box.insert(tk.END, "النظام جاهز للتشغيل...\n")

  def run_process(self):
    user_input = self.entry.get()
    if not user_input:
      messagebox.showwarning("تنبيه", "الرجاء إدخال بيانات صحيحة أولاً!")
    else:
      self.log_box.insert(tk.END, f">> جاري تنفيذ: {user_input}\n")
      self.entry.delete(0, tk.END)


if __name__ == "__main__":
  root = tk.Tk()
  app = SendarLiteApp(root)
  root.mainloop()
