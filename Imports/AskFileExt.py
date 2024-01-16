class AskFileExt:
    def extMenu(self):
        print("\nAvailable Extensions to Choose:\n"
            "-----------\n"
            "|   mp3   |\n"
            "|   m4a   |\n"
            "|   wav   |\n"
            "-----------\n")

    def askOGFileExt(self):
        while True:
            try:
                og_file_ext = str(input('Type Extension to Convert From, e.g "mp3"\n> '))
            except ValueError:
                print("Invalid Input. Try again.")
            else:
                return og_file_ext
            
    def askNewFileExt(self):
        while True:
            try:
                new_file_ext = str(input('Type Extension to Convert To, e.g "wav"\n> '))
            except ValueError:
                print("Invalid Input. Try again.")
            else:
                return new_file_ext

    def checkFileExt(self, ext):
        if ext not in ["mp3", "m4a", "wav"]:
            print("\nInvalid Format. Please Try Again.")
            return True
        else: 
            return False
        
    def askExt(self):
        self.extMenu()
        og_file_ext = self.askOGFileExt()
        while (self.checkFileExt(og_file_ext)):
            self.extMenu()
            og_file_ext = self.askOGFileExt()

        self.extMenu()
        new_file_ext = self.askNewFileExt()
        while (self.checkFileExt(new_file_ext)):
            self.extMenu()
            new_file_ext = self.askNewFileExt()
        
        return og_file_ext, new_file_ext