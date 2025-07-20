![World Capitals](./baner.png)

# 🌍 World Capitals Quiz 

A visually appealing, full-screen quiz game built with **Python (Tkinter + PIL + Pygame)**.  
Created by **VirusDesignStudio – Jasmin Kustura**.

## 🎮 Features

- ✅ Full-screen quiz with flag, capital and country questions
- 🌍 Questions grouped by continents (20 countries each)
- 🔊 Sound effects (correct/wrong) and background music
- 🖼️ Background world map with animated visuals
- 🧠 Timer for each question (10 seconds)
- 📦 One-click installable `.exe` version
- 📌 Credits & animated logo at bottom
- 💡 Designed for PC (Windows)

## 📁 Folder Structure

```
📁 WorldCapitals/
├── main.py                                  # Main app with resource_path()
├── countries_all_sample.json                # Capital & country data
├── mapa.webp                                # Background map image
├── Virus DS logo_.png                       # Logo image
├── backgroundsound.mp3                      # Background music
├── correct.wav / wrong.wav                  # Sound effects
├── app_icon.ico                             # App icon
├── worldcapitals.spec                       # PyInstaller spec
├── build_installer.bat                      # Batch script to build EXE
├── dist/WorldCapitals/                      # Built .exe and runtime files
└── WorldCapitals_Installer_FixedPath.iss    # Inno Setup script
```

## 🚀 How to Run (Python Version)

```bash
pip install pillow pygame
python main.py
```

## 🔧 How to Build .exe

1. Run: `build_installer.bat` or use `pyinstaller worldcapitals.spec`
2. Use `Inno Setup` with script `WorldCapitals_Installer_FixedPath.iss`
3. Result: `SetupWorldCapitals.exe` ready to distribute

## 📦 Dependencies

- Python 3.10+
- PIL (Pillow)
- Pygame
- Tkinter (comes with Python)

## ✨ Author

**Made by VirusDesignStudio – Jasmin Kustura**  
📧 info@virusdesignstudio.ba  
🔗 www.virusdesignstudio.ba

