import sublime_plugin

class RemoveFileCommentsCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        comments = self.view.find_by_selector('comment')
        for region in reversed(comments):
            comment = self.view.substr(region)
            line_breaks = ''.join(
                character for character in comment if character in '\r\n'
            )
            self.view.replace(edit, region, line_breaks)
