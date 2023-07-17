from model.xml_manager import PoleDataWriter
from view.app import App
import customtkinter as ctk


def main():
    # writer = PoleDataWriter('G:\\Shared drives\\2022 Booker Engineering\\CLIENTS\\TRACK UTILITIES\\O-CALC PROJECTS\\Pasco\\Deliverable\\H1001\\Permit 1\\Ocalc Files')
    # writer.write_to_excel()

    root = ctk.CTk()
    app = App(root)
    root.mainloop()


if __name__ == "__main__":
    main()
