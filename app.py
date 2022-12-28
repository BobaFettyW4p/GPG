import GetNovelText, pyperclip

from textual.reactive import reactive
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Button, Static
from textual.containers import Container


class App(App):
    
    BINDINGS = [('d','Toggle Dark Mode','toggle_dark')]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Container(PasswordGenerationButton())

    def exit_app(self) -> None:
        app.exit()
    
    def action_toggle_dark(self) -> None:
        self.dark = not self.dark

class PasswordGenerationButton(Static):
    def compose(self) -> ComposeResult:
        yield Button(label = "Generate Password",id = "generatePassword")

    def on_button_pressed(self, event:Button.Pressed) -> None:
        button_id = event.button.id
        if button_id == 'generatePassword':
            self.mount(PasswordCandidate())
        #this is a catch all if as password candidates will have ids in the format passwordCandidateX
        #where X is the position in the list; if we add a secret, more complex third button, this needs to be updated
        else:
            pyperclip.copy(str(event.button.label))

class PasswordCandidate(Static):
    def compose(self) -> ComposeResult:
        passwordCandidates = GetNovelText.main()
        for position,candidate in enumerate(passwordCandidates):
            yield Button(label= candidate, id=f'passwordCandidate{position}')
        
            


if __name__ == "__main__":
    app = App()
    app.run()
