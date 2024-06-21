import cx_Freeze

executables = [cx_Freeze.Executable("SillyRacing.py")]

cx_Freeze.setup(
    name = "Silly Lil Racecar",
    options = {"build_exe":{"packages":["pygame"],
                            "include_files":["racecar.png","Crash.wav","icon.png"]}},
    executables = executables
)
