import webbrowser
import Main.GUI.GUICentral as gui
import Main.GUI.MainAppLayout as appLayout


def main():
    mainApp = appLayout.build()
    mainApp.run_server(debug=True)

def open_browser():
    webbrowser.open_new('http://127.0.0.1:8050/')

if __name__ == '__main__':
    main()
