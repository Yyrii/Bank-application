
class Global_var():
    global_user_id = 0
    current_user_id = None

    def return_global_id(self):
        return self.global_user_id

    def return_current_id(self):
        return self.current_user_id

    def change_global_id(self,to):
        self.global_user_id = to

    def change_current_id(self,to):
        self.current_user_id = to
