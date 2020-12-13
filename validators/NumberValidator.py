from PyInquirer import Validator, ValidationError
class NumberValidator(Validator):
    def validate(self, document):
        try:
            int(document.text)
        except ValueError:
            raise ValidationError(
                message='Пожалуйста введите целое число',
                cursor_position=len(document.text))
