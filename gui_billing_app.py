try:
    import tkinter as tk
    from tkinter import messagebox
    from tkinter import ttk
except ModuleNotFoundError:
    print("Error: tkinter is not available in this environment.")
    exit(1)

import mysql.connector
from datetime import datetime

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'heheboi',
    'database': 'billing_project'
}

class LoginApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Billing System - Login")
        self.master.geometry("300x250")

        tk.Label(master, text="Username").pack(pady=5)
        self.username = tk.Entry(master)
        self.username.pack(pady=5)

        tk.Label(master, text="Password").pack(pady=5)
        self.password = tk.Entry(master, show="*")
        self.password.pack(pady=5)

        tk.Button(master, text="Login", command=self.login).pack(pady=10)
        tk.Button(master, text="Create Account", command=self.open_register).pack()

    def login(self):
        uname = self.username.get()
        passwd = self.password.get()

        try:
            con = mysql.connector.connect(**DB_CONFIG)
            cur = con.cursor()
            cur.execute("SELECT * FROM accounts WHERE user_name=%s AND password=%s", (uname, passwd))
            result = cur.fetchone()
            cur.close()
            con.close()

            if result:
                desig = result[4]
                messagebox.showinfo("Login Success", f"Welcome {uname}!")
                self.master.destroy()
                root = tk.Tk()
                DashboardApp(root, uname)
                root.mainloop()
            else:
                messagebox.showerror("Login Failed", "Invalid username or password")
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", str(e))

    def open_register(self):
        self.master.destroy()
        root = tk.Tk()
        RegisterApp(root)
        root.mainloop()

class RegisterApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Register Account")
        self.master.geometry("300x300")

        tk.Label(master, text="Username").pack(pady=5)
        self.username = tk.Entry(master)
        self.username.pack(pady=5)

        tk.Label(master, text="Password").pack(pady=5)
        self.password = tk.Entry(master, show="*")
        self.password.pack(pady=5)

        tk.Label(master, text="Designation (admin/staff/guest/customer)").pack(pady=5)
        self.designation = tk.Entry(master)
        self.designation.pack(pady=5)

        tk.Button(master, text="Register", command=self.register).pack(pady=10)

    def register(self):
        uname = self.username.get()
        passwd = self.password.get()
        desig = self.designation.get().lower()

        if desig not in ['admin', 'staff', 'guest', 'customer']:
            messagebox.showerror("Error", "Invalid designation.")
            return

        try:
            con = mysql.connector.connect(**DB_CONFIG)
            cur = con.cursor()
            cur.execute(
                "INSERT INTO accounts (user_name, password, date_created, desig) VALUES (%s, %s, CURDATE(), %s)",
                (uname, passwd, desig))
            con.commit()
            cur.close()
            con.close()
            messagebox.showinfo("Success", "Account created successfully")
            self.master.destroy()
            main()
        except mysql.connector.Error as e:
            messagebox.showerror("Error", str(e))

class DashboardApp:
    def __init__(self, master, username):
        self.master = master
        self.master.title("Dashboard")
        self.master.geometry("400x300")

        tk.Label(master, text=f"Welcome, {username}", font=('Arial', 14)).pack(pady=10)

        tk.Button(master, text="Add Product", width=20, command=self.add_product_window).pack(pady=5)
        tk.Button(master, text="View Products", width=20, command=self.view_products_window).pack(pady=5)
        tk.Button(master, text="Add to Bill", width=20, command=self.add_to_bill_window).pack(pady=5)
        tk.Button(master, text="Logout", width=20, command=self.logout).pack(pady=20)

    def add_product_window(self):
        win = tk.Toplevel(self.master)
        win.title("Add Product")
        win.geometry("300x250")

        tk.Label(win, text="Product Name").pack(pady=5)
        pname = tk.Entry(win)
        pname.pack(pady=5)

        tk.Label(win, text="Price").pack(pady=5)
        price = tk.Entry(win)
        price.pack(pady=5)

        tk.Label(win, text="PCP").pack(pady=5)
        pcp = tk.Entry(win)
        pcp.pack(pady=5)

        tk.Label(win, text="Stock Quantity").pack(pady=5)
        stock = tk.Entry(win)
        stock.pack(pady=5)

        def save_product():
            try:
                con = mysql.connector.connect(**DB_CONFIG)
                cur = con.cursor()
                cur.execute("INSERT INTO products (product_n, price, pcp, instock) VALUES (%s, %s, %s, %s)",
                            (pname.get(), price.get(), pcp.get(), stock.get()))
                con.commit()
                cur.close()
                con.close()
                messagebox.showinfo("Success", "Product added successfully")
                win.destroy()
            except mysql.connector.Error as e:
                messagebox.showerror("Database Error", str(e))

        tk.Button(win, text="Save", command=save_product).pack(pady=10)

    def view_products_window(self):
        win = tk.Toplevel(self.master)
        win.title("Product List")
        win.geometry("500x300")

        tree = ttk.Treeview(win, columns=("Name", "Price", "PCP", "Stock"), show='headings')
        tree.heading("Name", text="Product Name")
        tree.heading("Price", text="Price")
        tree.heading("PCP", text="PCP")
        tree.heading("Stock", text="Stock")
        tree.pack(fill=tk.BOTH, expand=True)

        try:
            con = mysql.connector.connect(**DB_CONFIG)
            cur = con.cursor()
            cur.execute("SELECT product_n, price, pcp, instock FROM products")
            for row in cur.fetchall():
                tree.insert('', tk.END, values=row)
            cur.close()
            con.close()
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", str(e))

    def add_to_bill_window(self):
        win = tk.Toplevel(self.master)
        win.title("Add to Bill")
        win.geometry("300x250")

        tk.Label(win, text="Product Name").pack(pady=5)
        pname = tk.Entry(win)
        pname.pack(pady=5)

        tk.Label(win, text="Price").pack(pady=5)
        price = tk.Entry(win)
        price.pack(pady=5)

        tk.Label(win, text="Quantity").pack(pady=5)
        quantity = tk.Entry(win)
        quantity.pack(pady=5)

        def save_bill():
            try:
                now = datetime.now()
                formatted = now.strftime('%Y-%m-%d %H:%M:%S')
                con = mysql.connector.connect(**DB_CONFIG)
                cur = con.cursor()
                cur.execute("INSERT INTO bill (p_name, price, quantity, d_o_p) VALUES (%s, %s, %s, %s)",
                            (pname.get(), price.get(), quantity.get(), formatted))
                con.commit()
                cur.close()
                con.close()
                messagebox.showinfo("Success", "Bill entry added successfully")
                win.destroy()
            except mysql.connector.Error as e:
                messagebox.showerror("Database Error", str(e))

        tk.Button(win, text="Add to Bill", command=save_bill).pack(pady=10)

    def logout(self):
        self.master.destroy()
        main()

def main():
    root = tk.Tk()
    LoginApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()
