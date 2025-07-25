class User:

    def __init__(self, user_name=None,user_email=None, user_password=None, user_job_title=None):
        self.name = user_name
        self.email = user_email
        self.password = user_password
        self.current_job_title = user_job_title


    def change_password(self, new_password):
        self.password = new_password

    def change_job_title(self, new_job_title):
        self.current_job_title = new_job_title

    def get_user_info(self):
        return f"User: {self.name}, Email: {self.email},password: {self.password}, Job Title: {self.current_job_title}"
