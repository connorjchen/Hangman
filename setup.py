import cx_Freeze

executables = [cx_Freeze.Executable("Hangman.py", base="Win32GUI",
                                    icon="hangmanLogo.ico", shortcutName="Hangman"
                                    , shortcutDir="DesktopFolder")]

cx_Freeze.setup(
    name="Hangman",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["img", "sound", "README.txt"]}},
    executables = executables

    )