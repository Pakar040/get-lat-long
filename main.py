from view.app import App
import customtkinter as ctk


def main():
    root = ctk.CTk()
    app = App(root)
    root.mainloop()


if __name__ == "__main__":
    main()
