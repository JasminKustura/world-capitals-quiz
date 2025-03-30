
[Setup]
AppName=World Capitals
AppVersion=1.0
DefaultDirName={pf}\WorldCapitals
DefaultGroupName=World Capitals
UninstallDisplayIcon={app}\WorldCapitals.exe
OutputDir=.
OutputBaseFilename=SetupWorldCapitals
Compression=lzma
SolidCompression=yes
SetupIconFile=app_icon.ico

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "Create a &desktop shortcut"; GroupDescription: "Additional icons:"; Flags: checkedonce

[Files]
Source: "WorldCapitals\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\World Capitals"; Filename: "{app}\WorldCapitals.exe"
Name: "{commondesktop}\World Capitals"; Filename: "{app}\WorldCapitals.exe"; Tasks: desktopicon
Name: "{group}\Uninstall World Capitals"; Filename: "{uninstallexe}"

[Run]
Filename: "{app}\WorldCapitals.exe"; Description: "Launch World Capitals"; Flags: nowait postinstall skipifsilent
