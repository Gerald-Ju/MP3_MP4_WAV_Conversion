import os

class Replace:
    def replace(self, file):
        replacements = {"（" : "(", "）" : ")", "—" : "",
                        "」" : ")", "「" : "(", "】" : ")",
                        "【" : "(", "[" : "(", "]" : ")", 
                        "–" : "-", " " : "_"}
        new_file = "".join([replacements.get(c, c) for c in file])   
        return new_file

    def replace_underscore(self, file):
        new_file = file.replace("_", " ")
        return new_file