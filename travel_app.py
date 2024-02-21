class AppServer:
    def call_database(self, request):
        pass
    def accepts_images(self):
        pass 
    def generate_image(self):
        pass
    def generate_text(self):
        pass

class TravelApp(AppServer):
    def get_user_name(self):
        return self.call_database('SELECT username...')

class TripImage(TravelApp):
    def return_image(self):
        if self.accepts_images():
            return self.generate_image(caption=self.set_caption())
        else:
            return self.generate_text()
    def set_caption(self):
        self.caption = f'Image by {self.get_user_name()}'