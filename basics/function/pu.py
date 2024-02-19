
def make_bold(func):
    def wrapper():
       
      return   f"<b>{func()}</b>"
      return wrapper


def make_italic(func):
     def wrapper():
       
      return f"<u>{func()}</u>"
      return wrapper



def make_underline(func):
      def wrapper():
       
       return  f"<i>{func()}</i>"
       return wrapper


@make_bold
@make_italic
@make_underline
def hello():
    return 'Hello world'
hello()
print()



