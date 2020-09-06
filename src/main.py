import eel
import glob

scoreDir = "C:\\Users\\whbt3\\MyDrive\\MyDevelop\\C#\\Tatelier\\Tatelier\\bin\\Debug\\Resources\\Score"



@eel.expose
def python_function():
    return glob.glob('{}/**/*.tja'.format(scoreDir), recursive=True)


eel.init('web')
eel.start('index.html', port=8018)