import tkinter as tk
import webbrowser

class WebLauncher:
    def __init__(self):
        self.sites = {
            "Google": "https://www.google.com",
            "YouTube": "https://www.youtube.com",
            "GitHub": "https://www.github.com",
            "Stack Overflow": "https://stackoverflow.com",
            "Wikipedia": "https://www.wikipedia.org"
        }

    def open_site(self, site_name):
        url = self.sites.get(site_name)
        if url:
            webbrowser.open(url)
        else:
            print("Site not found!")


class LauncherGUI:
    def __init__(self, root, launcher):
        self.launcher = launcher
        self.root = root
        self.root.title("Web Launcher")
        self.root.geometry("400x250")

        # Dropdown menu
        self.site_var = tk.StringVar(root)
        self.site_var.set("Google")
        self.dropdown = tk.OptionMenu(root, self.site_var, *self.launcher.sites.keys())
        self.dropdown.pack(pady=10)

        # Launch button
        self.launch_button = tk.Button(root, text="Launch Website", command=self.launch_site)
        self.launch_button.pack(pady=5)

        # Status label
        self.status_label = tk.Label(root, text="")
        self.status_label.pack(pady=10)

    def launch_site(self):
        site = self.site_var.get()
        self.launcher.open_site(site)
        self.status_label.config(text=f"Opening {site}...")


if __name__ == "__main__":
    launcher = WebLauncher()
    root = tk.Tk()
    app = LauncherGUI(root, launcher)
    root.mainloop()
