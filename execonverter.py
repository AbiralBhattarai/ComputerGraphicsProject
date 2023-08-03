import cx_Freeze

executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(
    name="PONG GAME",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["Readme.md"]}},
    executables = executables
    )