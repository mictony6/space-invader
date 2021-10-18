from cx_Freeze import setup, Executable

setup(name = "Space Invaders" ,
      version = "1.0.0" ,
      description = "My first game" ,
      executables = [Executable("PYTHON FILE", base = "Win32GUI")]
)